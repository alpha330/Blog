from django.core.exceptions import ValidationError
from django import forms
from .models.users import User
from .models.profile import Profile
from django.contrib.auth.forms import PasswordChangeForm


# Forms For Accounting In Blog


class RegistrationUser(forms.ModelForm):
    """
    This class is a form for user registration in the blog application.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def clean_password(self):
        # Check that the two passwords are equal
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class meta:
        model = Profile
        fields = ("first_name", "last_name", "description", "image")


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User  # Replace with the actual User model
        fields = ["old_password", "new_password1", "new_password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the form if needed
        self.fields["old_password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Old Password"}
        )
        self.fields["new_password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "New Password"}
        )
        self.fields["new_password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm New Password"}
        )
