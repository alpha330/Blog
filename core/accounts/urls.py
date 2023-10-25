from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "accounts"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('api/v1',include('accounts.api.v1.urls'),name='api_list_post'),
]