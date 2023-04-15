from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import PermissionDenied

MANAGEMENT = "Management"
SALES = "Sales"
SUPPORT = "Support"

MAXIMUM_TEAMS = 3


class Team(models.Model):
    name = models.CharField(_("Team name"), max_length=10)

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        if Team.objects.all().count() <= MAXIMUM_TEAMS or self.pk is not None:
            raise PermissionDenied(
                detail="You are not authorized to create a new team."
            )

    def delete(self, using=None, keep_parents=False):
        raise PermissionDenied(detail="You are not authorized to delete the team.")


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(_("First Name"), max_length=25, blank=False)
    last_name = models.CharField(_("Last Name"), max_length=25, blank=False)
    email = models.EmailField(_("Email address"), unique=True, blank=False)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    mobile = models.CharField(_("Mobile"), max_length=20, blank=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, default=1)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.team}"

    def save(self, *args, **kwargs):
        if self.team.name == MANAGEMENT:
            self.is_superuser = True
            self.is_staff = True

        if self.team.name == SALES or SUPPORT:
            self.is_staff = True

        user = super(User, self).save()

        return user
