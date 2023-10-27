from django.urls import path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = "api-v1"

urlpatterns = [
    # Registration
    path("registration/",views.RegistrationApiView.as_view(),name="registration"),
    
    
    # Change Password
    # Reset Password
    
    
    # Login Token
    path("token/login/",views.CustomAuthToken.as_view(),name="token-login"),
    path("token/logout/",views.CustomDiscardAuthToken.as_view(),name="token-logout")
    
    # Login JWT
    
]