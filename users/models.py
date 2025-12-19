from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

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
    certificate = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    experience = models.IntegerField()
    english_lvl = models.CharField(max_length=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
