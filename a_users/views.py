from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.utils import send_email_confirmation
from django.views.decorators.http import require_POST
from django_htmx.http import HttpResponseClientRefresh

from .models import UserProfile
from .forms import UserProfileForm, EmailForm


User = get_user_model()


def profile_view(request, username=None):

    if username is not None:
        profile = get_object_or_404(
            UserProfile.objects.select_related("user"), user__username=username
        )
    else:
        try:
            profile = request.user.userprofile
        except:
            return redirect_to_login(request.get_full_path())

    return render(request, "a_users/profile_view.html", {"profile": profile})


@login_required
def profile_edit(request):
    profile = get_object_or_404(
        UserProfile.objects.select_related("user"), user=request.user
    )

    form = UserProfileForm(instance=profile)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile-view")

    context = {
        "form": form,
    }
    return render(request, "a_users/profile_edit.html", context)


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


@require_POST
@login_required
def profile_avatar_img_delete(request):
    user_avatar = request.user.userprofile.avatar_img
    user_avatar.delete()

    if request.htmx:
        return HttpResponseClientRefresh()

    return redirect("profile-edit")


@login_required
def profile_email_change(request):

    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, "a_users/partials/email_form.html", {"form": form})

    if request.method == "POST":
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            email = form.cleaned_data["email"]

            if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                messages.warning(request, f"{email} is already in use.")
                return redirect("profile-settings")

            form.save()

            send_email_confirmation(request, request.user)

            return redirect("profile-settings")

        else:
            messages.warning(request, "Form not valid")
            return redirect("profile-settings")
