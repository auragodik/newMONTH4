from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
# Create your views here.


def CategoryView(request):
    categories = Category.objects.all()
    return render(request, "MyShop/categories.html", {"categories": categories})
    pass
def ProductView(request):
    products = Product.objects.all()
    return render(request, "MyShop/products.html", {"products": products})
    pass
def CategoryProducts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'MyShop/category_products.html', {
        "category": category,
        "products": products
    })
    pass    
    



