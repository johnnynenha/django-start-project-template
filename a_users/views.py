from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.utils import send_email_confirmation


@login_required
def profile_settings(request):
    return render(request, "a_users/profile_settings.html")


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect("profile-settings")


@login_required
def profile_delete(request):

    if request.method == "POST":
        user = request.user
        auth_logout(request)
        user.delete()
        messages.success(request, "Account deleted successfully.")
        return redirect("home")

    return render(request, "a_users/profile_delete.html")
