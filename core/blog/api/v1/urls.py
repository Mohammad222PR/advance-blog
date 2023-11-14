from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"


router = DefaultRouter()
router.register(r'post/post', views.PostListGeneric, basename='post')
router.register(r'post/cat', views.PostCategoryListGeneric, basename='cat')
router.register(r'post/tag', views.PostTagListGeneric, basename='tag')

urlpatterns = router.urls