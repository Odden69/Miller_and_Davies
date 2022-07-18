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

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
