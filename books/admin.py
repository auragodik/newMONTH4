from django.contrib import admin
from .models import AboutYou

@admin.register(AboutYou)
class AboutYouAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    search_fields = ('title', 'author')       
    list_filter = ('author',)                 
