from django.urls import path

from .views import profile_settings


urlpatterns = [
    path("settings/", profile_settings, name="profile-settings"),
]
