from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import Postform
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import Http404


class MyPostsList(LoginRequiredMixin, ListView):
    #permission_required = "blog.my_post_list"
    context_object_name = "posts"
    paginate_by = 20
    template_name = "blog/my_post_list.html"
    ordering = ["-created_date"]
    
    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author__user=user, status=True)
        return posts

    
class AllPostsList(LoginRequiredMixin, ListView):
    #permission_required = "blog.all_post_list"
    context_object_name = "posts"
    paginate_by = 20
    template_name = "blog/all_post_list.html"
    ordering = ["-created_date"]

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "author",
        "title",
        "content",
        "category",
        "status",
        "published_date",
    ]
    success_url = "/blog/post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = Postform
    success_url = ""
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # بررسی اینکه یوزر لاگین شده با نویسنده پست یکسان است یا نه
        if obj.author.user != self.request.user:
            raise Http404("You Do Not Have Permission To Edit This Post")
        return obj


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = ""
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # بررسی اینکه یوزر لاگین شده با نویسنده پست یکسان است یا نه
        if obj.author.user != self.request.user:
            raise Http404("You Do Not Have Permission To Delete This Post")
        return obj

class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"
