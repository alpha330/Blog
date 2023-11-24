from . import views
from rest_framework.routers import DefaultRouter

# urls configs

app_name = "api_v1"
router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls
