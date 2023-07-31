from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView
from .models import Post

# Create your views here.

# def indexview(request):
#     name = 'ali'
#     return render(request,'base.html',{'name':name})

class Indexview(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["post"] = Post.objects.all()
        return context
# def redirectToAli(request):
#     return redirect('https://alimahmoodi.net')

class RedirectToAli(RedirectView):
    url = 'https://alimahmoodi.net'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class PostList(ListView):
    #model = Post
    #queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all()
        return posts