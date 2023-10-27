from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='blog'),
    path('detail/<int:pk>', views.IndexPostDetail.as_view(), name='blog_detail'),
    # path('redirect', views.IndexRedirect.as_view(), name='redirect'),
    path('post/create', views.PostCreateView.as_view(), name='post_create_view'),

]