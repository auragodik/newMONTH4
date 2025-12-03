from django.contrib import admin
from .models import AboutYou

# Register your models here.
@admin.register(AboutYou)
class NewsAboutYouAdmin(admin.ModelAdmin):
    list_display = ('id',  'created_at')
    search_fields = ('jenre','author','day_made')
    list_filter = ('created_at',)
