from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

# Create your models here.


class CustomUserManager(UserManager):
    """
    Custom User Manager for setting email and password
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Connect method docstring: Brief description of the connect method.
        """
        if not email:
            raise ValueError("you have not provided a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    """
    Custom User-Model
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """
        
        """
        return self.email
