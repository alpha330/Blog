from django.test import SimpleTestCase,TestCase
from datetime import datetime
from blog.models import Post,Category
from blog.forms import Postform
from accounts.models import User,Profile
class TestPostForm(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com",password="123qwe!@#")
        self.profile_obj = Profile.objects.create(
            first_name="test", 
            last_name="testodi",
            user=self.user,
            created_date=datetime.now(), 
            description="for test purpose"
            )
        self.category = Category.objects.create(name="test-mode")
        
    def test_post_form_with_valid_data(self):
        form = Postform(data={
            "author":self.profile_obj, 
            "title":"test mode test", 
            "content":"test reason to write",
            "category":self.category, 
            "status":True,
            "published_date":datetime.now(),
        })
        self.assertTrue(form.is_valid())
        
    def test_post_form_without_valid_data(self):
        form = Postform(data={})
        self.assertFalse(form.is_valid())