from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


# Register your models here.
class CustomeUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_superuser", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permisions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_date", "created_date")
    list_filter = ("first_name", "last_name", "user")


admin.site.register(User, CustomeUserAdmin)
admin.site.register(Profile, ProfileAdmin)
