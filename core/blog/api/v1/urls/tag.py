from .. import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"


router = DefaultRouter()
router.register(r"post/tag", views.PostTagListGeneric, basename="tag")

urlpatterns = router.urls