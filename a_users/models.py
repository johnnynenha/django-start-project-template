from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_img = models.ImageField(
        _("avatar image"), upload_to="users_avatars/", null=True, blank=True
    )
    displayname = models.CharField(_("display name"), max_length=50, blank=True)
    info = models.TextField(_("info"), blank=True)

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("users profiles")
        ordering = [
            "user__username",
        ]

    @property
    def avatar_url(self):
        if self.avatar_img:
            return self.avatar_img.url
        return static("images/default_avatar.svg")

    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username


@receiver(post_save, sender=User)
def handle_userprofile_postsave(sender, instance, created, **kwargs):

    user = instance

    if created:
        UserProfile.objects.create(user=user)


@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()
