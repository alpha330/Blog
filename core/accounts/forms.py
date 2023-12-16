from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models.users import User

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
    
