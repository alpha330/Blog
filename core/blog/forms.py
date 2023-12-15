from django import forms
from blog.models import Post, Comments


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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["user", "comment"]
        