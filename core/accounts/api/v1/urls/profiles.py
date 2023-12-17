from django.urls import path
from .. import views

app_name = "api_v1_profile"
urlpatterns = [
    # Profile
    path("", views.ProfileApiView.as_view(), name="profile")
]
