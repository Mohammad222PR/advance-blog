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
from accounts.models.profiles import Profile
from .permissions import IsVerified
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
# imported library


# user
User = get_user_model()


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = Registerationserializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        """
        validate serializer for create new user`
        """
        serializer = Registerationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {
                "email": email,
            }
            """get user email and id for send activation email to user for verified account"""
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage("email/activation_email.tpl", {"token": token}, "admin@admin.com", to=[email],)
            EmailThread(email_obj).start()
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get_tokens_for_user(self, user):
        """generate access tokens(JWT) for a given user"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationResendApiView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            user_obj = get_object_or_404(User, email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/hello.tpl', {'token':token}, 'admin@admin.com', to=[email])
            EmailThread(email_obj).start()
            return Response({"detail":"email sended again"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail":"you dont have account please register account . if you miss your verify code can use this session"},
                  status=status.HTTP_400_BAD_REQUEST
                  )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(APIView):
    """verified account"""

    def get(self, request, token, *args, **kwargs):
        # decode token
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get('user_id')

        except ExpiredSignatureError:
            return Response({"details": "token has been expired"},status=status.HTTP_400_BAD_REQUEST,)

        except InvalidSignatureError:
            return Response({"details": "token is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        
        user_obj = get_object_or_404(User, pk=user_id)
        if user_obj.is_verified:
            return Response(data={'detail':'your account was verified'}, status=status.HTTP_400_BAD_REQUEST)
        user_obj.is_verified = True
        user_obj.save()
        return Response(data={'detail':'successfully now you have verified'}, status=status.HTTP_200_OK)



class CustomObtainAuthToken(ObtainAuthToken):
    """
    customObtainAuthToken for token now we have three out put field
    {
    token,
    user_id,
    email,
    }
    """

    serializer_class = CustomAuthTokenSerializer
    parser_classes = (MultiPartParser,)
    # permission_classes = [IsVerified]

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
                "email": user.email,
            }
        )


class CustomDiscardAuthToken(APIView):
    """
    discard user token if input your token you can delete your token id
    """

    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            {"detail": "your token delete successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


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
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong Password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password change successfully"},
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


# class TestEmailSendView(generics.GenericAPIView):

#     def get(self, request, *args, **kwargs):
#         self.email = 'mo123hammades13851@gmail.com'
#         user_obj = get_object_or_404(User, email = email_obj)
#         token = self.get_tokens_for_user(user_obj)
#         email_obj = EmailMessage('email/hello.tpl', {'token':token}, 'admin@admin.com', to=[self.email])
#         EmailThread(email_obj).start()
#         return Response({"detail":"email send"}, status=status.HTTP_200_OK)

#     def get_tokens_for_user(self, user):
#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)
