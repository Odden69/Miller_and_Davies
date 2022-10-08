from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
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
    favorites = request.session.get('favorites', [])
    page_number = 1
    query = None

    # category and subcategory filters
    if request.GET:
        page_number = request.GET.get('page')
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
        if 'favorites' in request.GET:
            products = products.filter(id__in=favorites)
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    paginator = Paginator(products, 20, orphans=3)
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
        'subcategories': subcategories,
        'selected_category': selected_category,
        'selected_subcategory': selected_subcategory,
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Returns a detail view of a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
