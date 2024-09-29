from django.urls import path

from .views import *


urlpatterns = [
    path("me/", profile_view, name="profile-view"),
    path("edit/", profile_edit, name="profile-edit"),
    path("settings/", profile_settings, name="profile-settings"),
    path("email_verify/", profile_emailverify, name="profile-emailverify"),
    path("delete/", profile_delete, name="profile-delete"),
    path("@<str:username>/", profile_view, name="profile-view-user"),
]
