from django.shortcuts import render, redirect
from .models import Product, Category, Subcategory


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
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    selected_category = None
    selected_subcategory = None

    if request.GET:
        if 'category' in request.GET:
            selected_category_name = request.GET['category']
            selected_category = categories.get(name=selected_category_name)
            products = products.filter(
                subcategory__category__name=selected_category_name)
            subcategories = subcategories.filter(
                category__name=selected_category)
            if 'subcategory' in request.GET:
                selected_subcategory_name = request.GET['subcategory']
                selected_subcategory = subcategories.get(
                    name=selected_subcategory_name)
                products = products.filter(
                    subcategory__name=selected_subcategory_name)

    context = {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
        'selected_category': selected_category,
        'selected_subcategory': selected_subcategory,

    }
    return render(request, 'products/products.html', context)
