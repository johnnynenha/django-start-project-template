from django import forms

from .models import UserProfile


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
        }
