from django.urls import path
from . import views
from django.urls import include

app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    #path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
