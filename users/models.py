from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import EmailField, CharField
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    email = EmailField(_("email address"), unique=True, blank=False, max_length=300)
    username = CharField(_("username"), unique=False, blank=False, max_length=300)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        super(CustomUserManager, self).create_user(email, email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return super(CustomUserManager, self).create_superuser(email, email, password, **extra_fields)
