from django.urls import path
from .. import views


urlpatterns = [
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
