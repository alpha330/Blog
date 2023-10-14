from django.urls import path
from . import views



#urls configs
app_name = "api_v1"

urlpatterns = [
    # path('/post',views.PostList.as_view(),name="post_list_api"),
    # path('/post/<int:pk>/',views.PostDetail.as_view(),name='api_post_detail_view'),
    path('/post',views.PostViewSet.as_view({'get':'list','post':'create'}),name="post_list_api"),
    path('/post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update'}),name='api_post_detail_view'),
]