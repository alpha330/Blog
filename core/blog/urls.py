from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path("cbv-index", views.Indexview.as_view(), name="cbv-index"),
    path("post/", views.PostList.as_view(), name="post_view"),
    path(
        "go-to-index/<int:pk>",
        views.RedirectToAli.as_view(pattern_name="blog:cbv-index"),
        name="go-to-cv",
    ),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create", views.PostCreateView.as_view(), name="create-post"),
    path("post/<int:pk>/edit", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete",
        views.DeletePostView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls"), name="api_list_post"),
]
