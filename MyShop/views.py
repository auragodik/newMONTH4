from django.shortcuts import render
from .models import Category, Product
# Create your views here.


def CategoryView(request):
    categories = Category.objects.all()
    return render(request, "categroies.html", {"categories": categories})

def ProductView(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def CategoryProducts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        "category": category,
        "products": products
    })
    

