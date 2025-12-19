from django.urls import path
from . import views

urlpatterns = [
    path('', views.PassView, name='home'),
    path('news_list/', views.newsPostView, name='news_list'),
    path('news_list/<int:id>/', views.PostDetailView, name='news_detail'),
    path('time/', views.CurrentTimeView, name='current_time'),
    path('writers/', views.WritersView, name='writerss'),
    path('citaty/', views.QuotesView, name='citatys'),
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
]
