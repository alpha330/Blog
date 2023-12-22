from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.MyPostsList.as_view(), name="my_post_view"),
    path("post/all-posts", views.AllPostsList.as_view(), name="all_post_view"),
    path("post/api-view/", views.PostListApiView.as_view(), name="post_view_api_view"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<str:category_name>", views.FilterByCategoryPostsList.as_view(), name="post-detail-by-category"),
    path(
        "post/<int:pk>/comment",
        views.CommentCreateView.as_view(),
        name="create-comment",
    ),
    path(
        "post/comment/reply/<int:post_pk>/<int:comment_pk>/",
        views.ReplyCreateView.as_view(),
        name="add_reply",
    ),
    path(
        "post/comment/<int:pk>/delete",
        views.CommentDeleteView.as_view(),
        name="delete-comment",
    ),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete",
        views.DeletePostView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls"), name="api_list_post"),
]
