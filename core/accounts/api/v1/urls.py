from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = "api-v1"

urlpatterns = [
    # Registration
    path("registration/",views.RegistrationApiView.as_view(),name="registration"),
    
    
    # Change Password
    # Reset Password
    
    
    # Login Token
    path("token/login/",views.CustomAuthToken.as_view(),name="token-login"),
    path("token/logout/",views.CustomDiscardAuthToken.as_view(),name="token-logout"),
    
    # Login JWT
    path("jwt/create/",views.CustomTokenObtainPairView.as_view(),name="jwt-create"),
    path("jwt/refresh/",TokenRefreshView.as_view(),name="jwt-refresh"),
    path("jwt/verify/",TokenVerifyView.as_view(),name="jwt-verify"),
]