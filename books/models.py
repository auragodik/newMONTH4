from django.db import models
from django.contrib.auth.models import User


mad_history = """ыя ыяыяыяыяя"""

class AboutYou(models.Model):
    author = models.CharField(verbose_name="Введи автора книги", max_length=100,default='Пусто')
    title = models.CharField(verbose_name='Введи название книги', max_length=200, default='Пусто')


    def __str__(self):
        return self.title
    

# class CustomUser(User):
#     first_name = models.CharField(verbose_name='your name')
#     surname = models.CharField(verbose_name='your surname')
#     GENDER = (
#         ('M', 'M')
#         ('F', 'F')
#         ('OTHER', 'OTHER')
#     )
#     gender = models.CharField(choices=GENDER, default="OTHER")
#     phone_number = models.CharField(max_length=13, verbose_name='your phone number')
#     city = models.CharField(max_length=100, verbose_name='your city', default='Bishkek')
#     CERTIFICATE = (
#         ('Secondary education', 'Secondary education')
#         ('Higher education', 'Higher education')
#         ('other', 'other')
#     )
#     certificate = models.CharField(max_length=100, choices=CERTIFICATE, default='other')
#     experience = models.PositiveIntegerField(max_length=100, default='None', verbose_name='your experience(in years)')
#     ENGLISH = (
#         ('A1', 'A1')
#         ('A2', 'A2')
#         ('B1', 'B1')
#         ('B2', 'B2')
#         ('C1', 'C1')
#         ('C1', 'C1')
#     )
#     english_lvl = models.CharField(max_length=100, choices=ENGLISH, default='A1')
#     favorite_book = models.CharField(max_length=100, verbose_name='favorite book')

#     def __str__(self):
#         return self.username