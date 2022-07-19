from django.shortcuts import render, redirect
from .models import Product


def index(request):
    """
    Redirects an empty url to products
    """
    return redirect('/products/')


def products(request):
    """
    Returns the products page
    """
    products = Product.objects.all()
    category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(subcategory__category__name=category)

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
