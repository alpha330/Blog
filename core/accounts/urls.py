from django.urls import path, include
from accounts import views
app_name = "accounts"

urlpatterns = [
    path("login/",views.LoginUser.as_view(), name="login"),
    path("registration/",views.RegistrationFromTemplateView.as_view(), name="register"),
    path("forget-password/",views.ForgetPasswordView.as_view(), name="forget-password"),
    path("reset-password/<str:token>",views.ResetPasswordViaLinkView.as_view(), name="reset-password-via-link"),
    path("verify-account/<str:token>",views.VerificationAccountView.as_view(), name="verify-account"),
    path("logout",views.LogOutView.as_view(), name="logout"),
    path("test/", views.test, name="test"),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
]
