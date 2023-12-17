from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .. import views

app_name = "api_v1_user"
# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # Registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path("test-email", views.TestEmailSend.as_view(), name="test-email"),
    # Activation
    path(
        "activate/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    # Resend Activation
    path(
        "activate/resend",
        views.ReconfirmationApiView.as_view(),
        name="reactivation",
    ),
    # Change Password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # Reset Password
    path(
        "send-reset-password-link/",
        views.ResetLinkPasswordSendApiView.as_view(),
        name="send-reset-password-link",
    ),
    path(
        "reset-password/<str:token>",
        views.ResetPasswordApiView.as_view(),
        name="reset-password",
    ),
    # Login Token
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # Login JWT
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    # Profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
