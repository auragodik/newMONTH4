from django.db import models



bad_history = """ssentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lor"""

class AboutYou(models.Model):
    author = models.CharField(verbose_name="enter author this book", max_length=100,default='unknown')
    day_made = models.IntegerField(verbose_name="when was created this book",default=2000)
    pages = models.IntegerField(verbose_name="enter how many pages",default=200)
    jenre = models.TextField(verbose_name="enter jenre",default='romcom')
    
    discription = models.TextField(
        verbose_name="enter your moment",
        max_length=500,
        default=''  ,
        blank=True         # bad_history у тебя не определён, поэтому пусть будет пусто
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    

