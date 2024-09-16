from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.utils import send_email_confirmation


@login_required
def profile_settings(request):
    return render(request, "a_users/profile_settings.html")


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect("profile-settings")
