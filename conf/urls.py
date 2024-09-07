from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", include("a_home.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()