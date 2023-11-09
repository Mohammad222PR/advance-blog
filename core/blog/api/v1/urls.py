from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"

urlpatterns = [
    # path("post/", views.PostList.as_view(), name="api-post-list"),

    path("post/detail/<int:pk>/", views.PostDetail.as_view(), name="api-post-detail"),
]

router = DefaultRouter()
router.register(r'post/viewset', views.PostListGeneric, basename='articles')
urlpatterns += router.urls