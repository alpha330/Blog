from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.urls import reverse


"""this is define post model for app blog """
""""""
User = get_user_model()


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def get_comment_count(self):
        return self.comments.count()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api_v1:post-detail", kwargs={"pk": self.pk})
    
# UPDATED PROJECT BLOG COMMENT SECTION IN MODEL APP BLOG
class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def get_comment_count(self):
        return self.comments.count()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
