from django.db import models
from django.contrib.auth.models import AbstractUser

CERTIFICATE = (
    ('Secondary education', 'Secondary education'),
    ('Higher education', 'Higher education'),
    ('other', 'other'),
)

GENDER = (
    ('M', 'M'),
    ('F', 'F'),
    ('OTHER', 'OTHER'),
)

ENGLISH = (
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    certificate = models.CharField(max_length=50, choices=CERTIFICATE)
    gender = models.CharField(max_length=10, choices=GENDER)
    city = models.CharField(max_length=50)
    experience = models.IntegerField()
    english_lvl = models.CharField(max_length=2, choices=ENGLISH)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
