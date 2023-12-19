from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# urls configs

app_name = "api_v1"
router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
router.register("comments", views.CommentViewSet, basename="comment")
router.register("replies", views.ReplyViewSet, basename="reply")

urlpatterns = router.urls
urlpatterns += [
    path('api/v1/comments/replies/', views.CommentViewSet.as_view({'get': 'replies'}), name='comment-replies'),
]