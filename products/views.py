from django.shortcuts import render, redirect


def index(request):
    """
    Redirects an empty url to products
    """
    return redirect('/products/')


def products(request):
    """
    Returns the products page
    """
    return render(request, 'products/products.html')
