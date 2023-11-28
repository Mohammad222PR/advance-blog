from django.urls import path
from . import views


app_name = "api-v1"

urlpatterns = [
    path("registration", views.RegistrationAPIView.as_view(), name="register_api_view"),
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token_login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token_logout"),

]
