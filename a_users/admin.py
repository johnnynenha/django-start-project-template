from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user__username", "get_avatar", "name", "info"]

    def get_avatar(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" alt="avatar image" style="object-fit:cover" />'.format(
                obj.avatar_url
            )
        )

    get_avatar.short_description = "Avatar"
