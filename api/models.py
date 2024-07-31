from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

import datetime

# Create your models here.


class CustomUserManager(UserManager):
    """
    Custom User Manager for setting email and password
    """

    def _create_user(self, email, password, username, **extra_fields):
        """
        Connect method docstring: Brief description of the connect method.
        """
        if not email:
            raise ValueError("you have not provided a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    """
    Custom User-Model
    """

    options = (
        ('Admin', 'admin'),
        ('Airline Staff', 'airline staff'),
        ('Airport Staff', 'airport staff'),
        ('Passenger', 'passenger'),
        ('Security Personnel', 'security personnel'),
        ('IT Support', 'IT support')
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    otp = models.IntegerField(max_length=4, default=0000)
    role = models.CharField(
        max_length=200, choices=options, default='Passenger')

    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        """

        """
        return self.email


class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.date.today)

    def __str__(self):
        """

        """
        return self.passport_number


class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure_location = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_location = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    aircraft = models.CharField(max_length=100)
    flight_duration = models.TimeField(default=datetime.time(5, 0))

    def __str__(self):
        return self.flight_number


class SeatClass(models.TextChoices):
    ECONOMY = 'E', 'Economy'
    BUSINESS = 'B', 'Business'
    FIRST_CLASS = 'F', 'First Class'


class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    seat_class = models.CharField(max_length=1, choices=SeatClass.choices)
    is_available = models.BooleanField(default=True)


class Reservation(models.Model):
    options = (
        ('CONFIRMED', 'Confirmed'),
        ('PROCESSING', 'Processing'),
        ('CANCELLED', 'Cancelled'),
    )

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=20, choices=options)

    def __str__(self):
        """

        """
        return self.status
