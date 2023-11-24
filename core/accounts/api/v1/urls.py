from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('registration', views.RegistrationAPIView.as_view(), name='register_api_view')
] 