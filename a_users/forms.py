from django import forms
from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["avatar_img", "displayname", "info"]
        widgets = {
            "avatar_img": forms.FileInput(
                attrs={
                    "oninput": "renderImage('avatar_img', this)",
                }
            ),
            "displayname": forms.TextInput(
                attrs={
                    "oninput": "renderText('profile_displayname', this)",
                }
            ),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email"]
