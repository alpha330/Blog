from django import forms
from .models import Post


class Postform(forms.ModelForm):
    
    class Meta :
        model = Post
        fields = ['title','content','category','status','published_date']

    
