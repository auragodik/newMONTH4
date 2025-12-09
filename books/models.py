from django.db import models



mad_history = """ыя ыяыяыяыяя"""

class AboutYou(models.Model):
    author = models.CharField(verbose_name="Введи автора книги", max_length=100,default='Пусто')
    title = models.CharField(verbose_name='Введи название книги', max_length=200, default='Пусто')


    def __str__(self):
        return self.title
    

