from django.test import TestCase
from datetime import datetime
from blog.models import Post, Category
from accounts.models import User, Profile


class TestModelPost(TestCase):
    def setUp(self):
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

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            title="Test Title",
            content="Test Content",
            category=self.category,
            author=self.profile,
            status=True,
            created_date=datetime.now(),
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
