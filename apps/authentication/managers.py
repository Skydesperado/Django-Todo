from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError(_("The Email Field Must Be Set"))
        if not first_name:
            raise ValueError(_("The First Name Field Must Be Set"))
        if not last_name:
            raise ValueError(_("The Last Name Field Must Be Set"))
        user = self.model(email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
