from django.core.exceptions import ValidationError
from django import forms
from .models.users import User
from .models.profile import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext_lazy as _


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
        
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_('Old Password'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    class Meta:
        model = User  # Assuming your custom user model is named 'User'
        fields = ('old_password', 'new_password1', 'new_password2')
        
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('The new passwords do not match.')

        return cleaned_data
    
    
