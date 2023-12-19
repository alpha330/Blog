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
        fields = ['comment','image',]  # You can add more fields if you need
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your comment here'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        