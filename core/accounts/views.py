from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.views.decorators.cache import cache_page
from .models import Profile, User
from .forms import ChangePasswordForm

# Create your views here.


@cache_page(60 * 15)
def test(request):
    Response = requests.get(
        "https://a89d010f-1b29-4211-b34b-0ce6c63ed80e.mock.pstmn.io/test/delay/5"
    )
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


class RegistrationFromTemplateView(View):
    template_name = "registration/registration.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        api_url = reverse_lazy("accounts:api_v1_user:registration")
        absolute_url = request.build_absolute_uri(api_url)
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "password1": request.POST.get("password1"),
        }

        response = requests.post(absolute_url, data=data)
        if response.status_code == 201:
            return redirect("/")
        else:
            return render(request, self.template_name, {"error": True})


class ForgetPasswordView(View):
    template_name = "registration/forget-password.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        api_url = reverse_lazy("accounts:api_v1_user:send-reset-password-link")
        absolute_url = request.build_absolute_uri(api_url)
        data = {
            "email": request.POST.get("email"),
        }
        response = requests.post(absolute_url, data=data)
        if response.status_code == 200:
            return render(request, self.template_name, {"success": True})
        else:
            return render(request, self.template_name, {"error": True})


class ResetPasswordViaLinkView(View):
    template_name = "registration/reset-password-via-link.html"

    def get(self, request, *args, **kwargs):
        return reverse_lazy(request, self.template_name)

    def post(self, request, *args, **kwargs):
        token = kwargs.get("token")
        api_url = reverse_lazy(
            "accounts:api_v1_user:reset-password", kwargs={"token": token}
        )
        absolute_url = request.build_absolute_uri(api_url)
        data = {
            "new_password": request.POST.get("password"),
            "new_password_1": request.POST.get("password1"),
        }
        response = requests.put(absolute_url, data=data)
        if response.status_code == 200:
            return redirect("accounts:login")
        else:
            return render(request, self.template_name, {"error": True})


class VerificationAccountView(View):
    template_name_success = "registration/account-verified.html"
    template_name_fail = "registration/account-verified-fail.html"

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        api_url = reverse_lazy(
            "accounts:api_v1_user:activation", kwargs={"token": token}
        )
        absolute_url = request.build_absolute_uri(api_url)
        response = requests.get(absolute_url)

        if response.status_code == 200:
            return render(request, self.template_name_success)
        else:
            return render(request, self.template_name_fail)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "registration/profile.html"
    context_object_name = "user_profile"

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile-edit.html"
    model = Profile
    fields = [
        "first_name",
        "last_name",
        "description",
        "image",
    ]
    success_url = reverse_lazy("accounts:profile-view")


class LogOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("accounts:login")
        return redirect("accounts:login")


class ChangePasswordView(LoginRequiredMixin, UpdateView):
    template_name = "registration/password-change.html"
    form_class = ChangePasswordForm
    model = User
    success_url = reverse_lazy("accounts:profile-view")

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop("instance", None)
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Password successfully changed.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Password change failed. Please correct the errors."
        )
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return render(request, self.template_name, {"form": form})
