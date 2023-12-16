from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse
import requests
from django.views.decorators.cache import cache_page
from .forms import RegistrationUser
# Create your views here.


@cache_page(60 * 15)
def test(request):
    Response = requests.get("https://a89d010f-1b29-4211-b34b-0ce6c63ed80e.mock.pstmn.io/test/delay/5")
    return JsonResponse(Response.json())

class LoginUser(LoginView):
    """
    view class with parent LoginView in auth views
    rewrite Attributes :
    template_name , Fields,Redirect if user authenticated
    """

    template_name = "registration/login.html"
    fields = "email", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        """
        def to reverse urls name if login successful
        """
        return reverse_lazy("blog:all_post_view")
    
class RegistrationView(FormView):
    template_name = "registration/registration.html"
    redirect_authenticated_user = True
    form_class = RegistrationUser
    success_url = reverse_lazy("blog:all_post_view")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)
    
class LogOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('accounts:login')
        return redirect('accounts:login')