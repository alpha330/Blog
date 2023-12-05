from django.shortcuts import get_object_or_404
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


class Indexview(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["post"] = Post.objects.all()
        return context


class RedirectToAli(RedirectView):
    url = "https://alimahmoodi.net"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    context_object_name = "posts"
    paginate_by = 2
    ordering = ["-id"]

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
    success_url = "/blog/post"


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post"
    
class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"
