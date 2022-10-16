from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Subcategory
from .forms import ProductForm


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
        if 'bargains' in request.GET:
            products = products.filter(on_sale=True)
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)
    for product in products:
        if product.on_sale:
            product.on_sale_price = \
                round(product.price-product.discount*product.price/100, 2)

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
    if product.on_sale:
        product.on_sale_price = \
            round(product.price-product.discount*product.price/100, 2)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    redirect_url = request.POST.get('redirect_url')

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only a store owner can add a product.')
        return redirect(redirect_url)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'Successfully added {product.name} to the store!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product. \
Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only a store owner can edit a product.')
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. \
Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}.')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a specific product from the store """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only a store owner can delete a product.')
        return redirect('home')
    product.delete()
    messages.success(request, 'Product was deleted!')
    return redirect('home')
