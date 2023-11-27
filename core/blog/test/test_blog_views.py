from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from blog.models import Post, Category
from accounts.models import User, Profile


class TestBlogViews(TestCase):
    def setUp(self):
        self.Client = Client()
        self.user = User.objects.create_user(
            email="test@test.com", password="123qwe!@#"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test",
            last_name="testi",
            description="test123",
            created_date=datetime.now(),
        )
        self.category = Category.objects.create(name="test-category")
        self.post = Post.objects.create(
            title="Test Title",
            content="Test Content",
            category=self.category,
            author=self.profile,
            status=True,
            created_date=datetime.now(),
            published_date=datetime.now(),
        )

    def test_blog_index_url_successful_response(self):
        url = reverse("blog:cbv-index")
        response = self.Client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, template_name="base.html")

    def test_blog_post_detail_loged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
