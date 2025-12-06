from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView, name='categories'),
    path('products/', views.ProductView, name='product'),
    path('categories/<int:category_id>/', views.CategoryProducts, name="category_products"),
]