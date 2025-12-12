from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='your name')
    surname = models.CharField(max_length=150, verbose_name='your surname')

    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
        ('OTHER', 'OTHER'),
    )
    gender = models.CharField(max_length=6, choices=GENDER, default="OTHER")

    phone_number = models.CharField(max_length=13, verbose_name='your phone number')

    city = models.CharField(max_length=100, verbose_name='your city', default='Bishkek')

    CERTIFICATE = (
        ('Secondary education', 'Secondary education'),
        ('Higher education', 'Higher education'),
        ('other', 'other'),
    )
    certificate = models.CharField(max_length=30, choices=CERTIFICATE, default='other')

    experience = models.PositiveIntegerField(default=0, verbose_name='your experience(in years)')

    ENGLISH = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )
    english_lvl = models.CharField(max_length=2, choices=ENGLISH, default='A1')

    favorite_book = models.CharField(max_length=100, verbose_name='favorite book')

    def __str__(self):
        return self.username
