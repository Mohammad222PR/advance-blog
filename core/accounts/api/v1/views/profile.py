from rest_framework import generics
from ..serializers.profile import (
    ProfileSerializer,
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models.profiles import Profile
import requests
# from mail_templated import send_mail



# imported library



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


class CacheView(APIView):
    @method_decorator(cache_page(60, key_prefix="cache-view"))
    def get(self, request):
        response = requests.get('https://a9f6156f-b274-4522-88af-a2df25158396.mock.pstmn.io/test/delay/5')
        return Response({'detail': response.json()})