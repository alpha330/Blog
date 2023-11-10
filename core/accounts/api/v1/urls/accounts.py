from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    # Registration
    path("registration/",views.RegistrationApiView.as_view(),name="registration"),
    path("test-email",views.TestEmailSend.as_view(),name="test-email"),
    
    # Activation
    #path("activate/confirm")
    
    # Resend Activation
     #path("activate/resend")
    
    # Change Password
    path('change-password/',views.ChangePasswordApiView.as_view(),name="change-password"),
    
    # Reset Password
    
    
    # Login Token
    path("token/login/",views.CustomAuthToken.as_view(),name="token-login"),
    path("token/logout/",views.CustomDiscardAuthToken.as_view(),name="token-logout"),
    
    # Login JWT
    path("jwt/create/",views.CustomTokenObtainPairView.as_view(),name="jwt-create"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="jwt-refresh"),
    path("jwt/verify/",TokenVerifyView.as_view(),name="jwt-verify"),
    # Profile
    path("profile/",views.ProfileApiView.as_view(),name="profile")
]