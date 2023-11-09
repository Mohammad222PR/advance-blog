from django.urls import path
from . import views


app_name = "api-v1"

urlpatterns = [
    # path("post/", views.PostList.as_view(), name="api-post-list"),
    path("post_list/", views.PostListGeneric.as_view(), name="api-post-liwest"),

    path("post/detail/<int:pk>/", views.PostDetail.as_view(), name="api-post-detail"),
]
