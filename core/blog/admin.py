from django.contrib import admin
from .models import Post, Category, Comments

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_date",
        "published_date",
    ]
    list_filter = [
        "status",
        "category__name",
        "author",
        "created_date",
        "published_date",
    ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "post",
        "created_date",
        "updated_date",
        "parent",
    ]
    list_filter = [
        "user",
        "post",
        "created_date",
        "updated_date",
        "parent",
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Category, CategoryAdmin)
