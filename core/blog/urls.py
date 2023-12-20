from django.urls import path
from . import views
from django.urls import include


app_name = "blog"

urlpatterns = [
    path("index", views.IndexView.as_view(), name="index"),
    path("", views.PostView.as_view(), name="blog"),
    path(
        "post-detail/<int:pk>",
        views.PostDetailView.as_view(),
        name="post-detail",
    ),
    path("post/list/api/", views.PostListApiView.as_view(), name="post-api-view"),

    path("redirect", views.IndexRedirect.as_view(), name="redirect"),
    path(
        "post/create",
        views.PostCreateView.as_view(),
        name="post_create_view",
    ),
    path(
        "post/update/<int:pk>",
        views.PostUpdateView.as_view(),
        name="post_update_view",
    ),
    path(
        "post/<int:id>/delete",
        views.DeleteView.as_view(),
        name="post_delete_view",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
