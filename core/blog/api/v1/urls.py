from django.urls import path
from . import views


#urls configs
app_name = "api_v1"

urlpatterns = [
    path('/post',views.postlist,name='api_post_view')

]