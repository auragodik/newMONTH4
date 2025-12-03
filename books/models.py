from django.db import models



mad_history = """ыя ыяыяыяыяя"""

class AboutYou(models.Model):
    author = models.CharField(verbose_name="Введи автора книги", max_length=100,default='Пусто')
    day_made = models.IntegerField(verbose_name="Когда написано",default=2000)
    pages = models.IntegerField(verbose_name="Сколько страниц",default=200)
    jenre = models.TextField(verbose_name="Жанр",default='роман')
    
    discription = models.TextField(
        verbose_name="enter your moment",
        max_length=500,
        default=''  ,
        blank=True         # bad_history у тебя не определён, поэтому пусть будет пусто
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    

