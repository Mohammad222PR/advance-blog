from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('registration', views.RegisterAPIView.as_view(), name='register_api_view')
] 