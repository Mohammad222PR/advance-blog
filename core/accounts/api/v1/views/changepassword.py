from rest_framework import generics
from ..serializers.change_password import (
    ChangePasswordSerializer,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ...utils import EmailThread
from django.contrib.auth import get_user_model


# imported library

User = get_user_model()


class ResetPasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_obj = request.user
        email_obj = EmailMessage(
            "email/activation_email.tpl",
            {"message": "click"},
            "admin@admin.com",
            to=[user_obj.email],
        )
        EmailThread(email_obj).start()
        return Response(data={"detail": "email sended"}, status=status.HTTP_200_OK)


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
