from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    PostDetailView,
    AllPostsList,
    MyPostsList,
    PostListApiView,
    CommentCreateView,
    ReplyCreateView,
    CommentDeleteView,
    PostCreateView,
    PostEditView,
    DeletePostView,
)

# Create your tests here.


class TestUrl(SimpleTestCase):
    # def test_blog_index_url_resolve(self):
    #     url = reverse("blog:cbv-index")
    #     self.assertEqual(resolve(url).func.view_class, Indexview)

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:all_post_view")
        self.assertEqual(resolve(url).func.view_class, AllPostsList)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_blog_my_post_url_resolve(self):
        url = reverse("blog:my_post_view")
        self.assertEqual(resolve(url).func.view_class, MyPostsList)

    def test_blog_post_api_view_url_resolve(self):
        url = reverse("blog:post_view_api_view")
        self.assertEqual(resolve(url).func.view_class, PostListApiView)

    def test_blog_comment_create_url_resolve(self):
        url = reverse("blog:create-comment", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, CommentCreateView)

    def test_blog_reply_to_comment_url_resolve(self):
        url = reverse("blog:add_reply", kwargs={"post_pk": 1, "comment_pk": 1})
        self.assertEqual(resolve(url).func.view_class, ReplyCreateView)

    def test_blog_comment_delete_url_resolve(self):
        url = reverse("blog:delete-comment", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, CommentDeleteView)

    def test_blog_post_create_url_resolve(self):
        url = reverse("blog:post-create")
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_blog_post_edit_url_resolve(self):
        url = reverse("blog:post-edit", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostEditView)

    def test_blog_post_delete_url_resolve(self):
        url = reverse("blog:post-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, DeletePostView)
