from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from blog.views import Indexview,PostList,PostDetailView
# Create your tests here.

class TestUrl(SimpleTestCase):
    
    def test_blog_index_url_resolve(self):
        url = reverse("blog:cbv-index")
        self.assertEqual(resolve(url).func.view_class,Indexview)
    
    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post_view")
        self.assertEqual(resolve(url).func.view_class,PostList)
    
    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail",kwargs={"pk":1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView)