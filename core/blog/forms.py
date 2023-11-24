from django import forms
from .models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "content",
            "category",
            "status",
            "published_date",
        ]
