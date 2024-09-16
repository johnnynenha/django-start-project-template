from django.urls import path

from .views import *


urlpatterns = [
    path("settings/", profile_settings, name="profile-settings"),
    path("email_verify/", profile_emailverify, name="profile-emailverify"),
    path("delete/", profile_delete, name="profile-delete"),
]
