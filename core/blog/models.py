from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#getting user model object
# user = get_user_model()

'''this is define post model for app blog '''
''''''
class Post(models.Model):
    image =models.ImageField(null=True,blank=True)
    author = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)
    published_date =models.DateTimeField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
