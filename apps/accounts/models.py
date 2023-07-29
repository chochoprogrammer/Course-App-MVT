import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStamp
from apps.accounts.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=(_("First name")), max_length=25, null=True)
    last_name = models.CharField(verbose_name=(_("Last name")), max_length=25, null=True)
    email = models.EmailField(verbose_name=(_("Email address")), unique=True)
    # avatar = models.ImageField(upload_to="bidout-auction-v1/avatars/", null=True)

    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def avatarURL(self):
    #     try:
    #         url = self.avatar.url
    #     except:
    #         url = "https://res.cloudinary.com/kay-development/image/upload/v1679787683/important/brad_dozo7x.jpg"
    #     return url

    def __str__(self):
        return self.full_name
