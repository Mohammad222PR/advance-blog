from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.indexView.as_view(), name='blog'),
    path('detail/<int:pk>', views.IndexPostDetail.as_view(), name='blog_detail'),
    path('redirect', views.IndexRedirect.as_view(), name='redirect'),

]