from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("a_home.urls")),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("a_users.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
