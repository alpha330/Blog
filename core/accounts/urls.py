from django.urls import path, include
from accounts import views
app_name = "accounts"

urlpatterns = [
    path("login/",views.LoginUser.as_view(), name="login"),
    path("registration/",views.RegistrationView.as_view(), name="register"),
    path("logout",views.LogOutView.as_view(), name="logout"),
    path("test/", views.test, name="test"),
    path("api/v1/", include("accounts.api.v1.urls"), name="api_list_post"),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
