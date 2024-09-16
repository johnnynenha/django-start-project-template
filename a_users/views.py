from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile_settings(request):
    return render(request, "a_users/profile_settings.html")
