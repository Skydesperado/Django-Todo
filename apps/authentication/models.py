import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(unique=True,
                            default=uuid.uuid4,
                            verbose_name=_("UUID"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Admin"))

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
