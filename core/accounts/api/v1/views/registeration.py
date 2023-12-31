from rest_framework import generics
from ..serializers.register_login import (
    Registerationserializer,
    ActivationResendSerializer,
    LoginSerializer,
)
from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ...utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
)

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
            """
            get user email and id for send activation email to user for verified account
            """
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation_email.tpl",
                {"token": token},
                "admin@admin.com",
                to=[email],
            )
            EmailThread(email_obj).start()
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get_tokens_for_user(self, user):
        """
        generate access tokens(JWT) for a given user
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            user = authenticate(email=cd["email"], password=cd["password"])
            if user is not None:
                login(request, user)
                return Response(
                    {"email": user.email, "id": user.id},
                    status=status.HTTP_200_OK,
                )


class ActivationResendApiView(generics.GenericAPIView):
    serializer_class = ActivationResendSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        serializers = ActivationResendSerializer(data=request.data)
        if serializers.is_valid():
            user_obj = serializers.validated_data["user"]
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/hello.tpl",
                {"token": token},
                "admin@admin.com",
                to=[user_obj.email],
            )
            EmailThread(email_obj).start()
            return Response(
                {"detail": "email sended again"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "request failed"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(APIView):
    """
    verified account
    """

    def get(self, request, token, *args, **kwargs):
        # decode token
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")

        except ExpiredSignatureError:
            return Response(
                {"details": "token has been expired"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except InvalidSignatureError:
            return Response(
                {"details": "token is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_obj = get_object_or_404(User, pk=user_id)
        if user_obj.is_verified:
            return Response(
                data={"detail": "your account was verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user_obj.is_verified = True
        user_obj.save()
        return Response(
            data={"detail": "successfully now you have verified"},
            status=status.HTTP_200_OK,
        )

