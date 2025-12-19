from django.urls import path
from . import views

urlpatterns = [
    path('', views.PassView.as_view(), name='home'), 
    path('news_list/', views.NewsPostView.as_view(), name='news_list'),
    path('news_list/<int:id>/', views.PostDetailView.as_view(), name='news_detail'), 
    path('time/', views.CurrentTimeView.as_view(), name='current_time'),  
    path('writers/', views.WritersView.as_view(), name='writerss'),  
    path('citaty/', views.QuotesView.as_view(), name='citatys'),
    path('books/', views.BookListView.as_view, name='book_list'), 
    path('books/create/', views.BookCreateView.as_view(), name='book_create'), 
]
