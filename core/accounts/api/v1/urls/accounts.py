from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # default:
    path("registration", views.RegistrationAPIView.as_view(), name="register-api-view"),

    # token:
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),

    # jwt:
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),

    # change password:
    path('password-change/', views.ChangePasswordApiView.as_view(), name="password-change"),

    # # activation user:
    # path('user/activation/confirm/', views.UserConfirmView.as_view(), name="user-activation-confirm"),

    # # Resend activation:
    # path('user/activation/resend/', views.ResendConfirmView.as_view(), name="user-activation-resend"),

    # test:
    path('test-email/', views.TestEmailSendView.as_view(), name="test-email"),

]
