from django.urls import path
from . import views

urlpatterns = [
    path('weather/info/', views.index),  #the path for our index view
]