from django.urls import path

from .views import *


urlpatterns = [
    path("me/", profile_view, name="profile-view"),
    path("edit/", profile_edit, name="profile-edit"),
    path("settings/", profile_settings, name="profile-settings"),
    path("email_verify/", profile_emailverify, name="profile-emailverify"),
    path("email_change/", profile_email_change, name="profile-email-change"),
    path("delete/", profile_delete, name="profile-delete"),
    path(
        "delete_avatar_image/",
        profile_avatar_img_delete,
        name="profile-delete-avatar-image",
    ),
    path("@<str:username>/", profile_view, name="profile-view-user"),
]
