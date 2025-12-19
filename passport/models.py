from django.db import models
from django.conf import settings

class Passport(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.number}"
