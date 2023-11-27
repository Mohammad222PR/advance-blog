from rest_framework import generics
from .serialiezers import Registerationserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer

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

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
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
