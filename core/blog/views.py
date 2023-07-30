from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.

def indexview(request):
    name = 'ali'
    return render(request,'base.html',{'name':name})

class Indexview(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["post"] = Post.objects.all()
        return context
