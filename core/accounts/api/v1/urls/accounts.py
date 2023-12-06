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
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name="activation"),

    # # Resend activation:
    path('activation/resend/', views.ActivationResendApiView.as_view(), name="-activation-resend"),

    # test email:
    # path('test-email/', views.TestEmailSendView.as_view(), name="test-email"),

]
