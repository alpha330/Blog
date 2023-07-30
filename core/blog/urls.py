from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    # [...]
    path('fb-index',views.indexview,name='fb-viewtest'),
    #path('cbv-index/', TemplateView.as_view(template_name='base.html',extra_context={"name":"ali"})),
    path('cbv-index',views.Indexview.as_view(),name='cbv-index'),
    path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index'), name='go-to-cv'),

]