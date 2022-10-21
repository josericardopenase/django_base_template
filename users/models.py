from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from utils.integrations.holded.models import HoldedEmployee
from utils.models import BaseModel
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .teachers.models import TeacherProfile
from .secretaries.models import SecretaryProfile
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


USER_TYPES = [
    ("TEACHER", "Teacher"),
    ("STUDENT", "Student"),
    ("SECRETARY", "Secretary"),
    ("MANAGER", "Manager"),
    ("OWNER", "Owner"),
]

# Create your models here.
class User(AbstractUser, HoldedEmployee, BaseModel):
    username = models.CharField(max_length=200, unique=False)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    avatar = models.ImageField(blank=True, null=True)

    objects = CustomUserManager()
    role = models.CharField(max_length=200, unique=False, choices=USER_TYPES)
    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="company",
    )

    offices = models.ManyToManyField("offices.Office", related_name="employees")
    dni = models.CharField(max_length=8)
    phone_number = PhoneNumberField(_("phone_number"), blank=False)

    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default="#FFFFFF")

    def __str__(self):
        return self.email

    @property
    def name(self):
        return self.get_full_name() if self.get_full_name() else self.email

    def set_random_password(self):
        password = User.objects.make_random_password()
        self.set_password(password)
        self.save()
        return password

    def create_profile(self):
        if self.role == "TEACHER":
            TeacherProfile(user=self).save()
        elif self.role == "SECRETARY":
            SecretaryProfile(user=self).save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        instance.create_profile()
        instance.create_holded_profile()
        Token.objects.create(user=instance)


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_holded_profile(sender, instance=None, **kwargs):
    if instance.has_holded_profile:
        instance.delete_holded_profile()
