from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=30)


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

