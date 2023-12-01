from rest_framework import generics
from .serialiezers import (
    Registerationserializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializers,
    ChangePasswordSerializer,
    ProfileSerializer,
)
from django.shortcuts import render, get_object_or_404

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from accounts.models import Profile
# imported library

User = get_user_model()


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = Registerationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "email": serializer.validated_data["email"],
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "email": user.email
            }
        )


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)


    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail':'your token delete successfully'},status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializers
    parser_classes = (MultiPartParser,)


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    parser_classes = (MultiPartParser,)

    def get_object(self):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong Password']}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'details':'password change successfully'}, status=status.HTTP_202_ACCEPTED)        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ProfileApiView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj