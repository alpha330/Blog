from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Usermanager(BaseUserManager):
    """
    User manager for customeuser model app accounts
    """
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('Email cannot be blank'))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_verified',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have staff permissions"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have superuser permissions"))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model with basic fields and methods for authentication
    """
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    objects = Usermanager()

    def __str__(self):
        return self.email