from .. import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"post/post", views.PostListGeneric, basename="post")

urlpatterns = router.urls
