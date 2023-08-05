from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    # [...]
    #path('fb-index',views.indexview,name='fb-viewtest'),
    #path('cbv-index/', TemplateView.as_view(template_name='base.html',extra_context={"name":"ali"})),
    path('cbv-index',views.Indexview.as_view(),name='cbv-index'),
    path('post/',views.PostList.as_view(),name='post_view'),
    path('go-to-index/<int:pk>', views.RedirectToAli.as_view(pattern_name='blog:cbv-index'), name='go-to-cv'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post-detail'),
    path('post/create',views.PostCreateView.as_view(),name='create-post'),
    path('post/<int:pk>/edit',views.PostEditView.as_view(),name='post-edit'),
    path('post/<int:pk>/delete',views.DeletePostView.as_view(),name='post-delete'),
]