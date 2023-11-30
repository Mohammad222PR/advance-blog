from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1"

urlpatterns = [
    # Default
    path("registration", views.RegistrationAPIView.as_view(), name="register-api-view"),
    # Token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # JWT
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenRefreshView.as_view(), name="jwt-verify"),
    #Reset Password
    path('password-change/', views.ChangePasswordApiView.as_view(), name="password-change"),
]
