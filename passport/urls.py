from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('add/', views.add_passport, name='add_passport'),
    path('success/', lambda request: render(request, 'passport/success.html'), name='passport_success'),
]
