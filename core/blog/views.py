from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comments
from .forms import Postform,CommentForm
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
    context_object_name = 'post'
    template_name = "blog/post_detail_comments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        comments = Comments.objects.filter(post=post)
        context['comments'] = comments
        return context


    def get_success_url(self):
        return self.request.path



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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.parent = None  # Assume that we're creating a top-level comment
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.post.pk})
    
class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'blog/add_reply.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        form.instance.parent_id = self.kwargs['comment_pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.post.pk})
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)