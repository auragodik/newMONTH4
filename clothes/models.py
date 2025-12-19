from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Clothes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Balenciaga - Its different')
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return f'{self.title}-{", ".join(i.name for i in self.categories.all())}'