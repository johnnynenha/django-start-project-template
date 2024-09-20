from django.urls import path

from .views import *


urlpatterns = [
    path("", profile_view, name="profile-view"),
    path("settings/", profile_settings, name="profile-settings"),
    path("email_verify/", profile_emailverify, name="profile-emailverify"),
    path("delete/", profile_delete, name="profile-delete"),
]
