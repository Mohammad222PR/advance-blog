from .. import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r"post/cat", views.PostCategoryListGeneric, basename="cat")

urlpatterns = router.urls