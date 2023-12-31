from ..serializers.obtaintoken import (
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializers,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
# from mail_templated import send_mail
from mail_templated import EmailMessage
from ...utils import EmailThread


# imported library


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



