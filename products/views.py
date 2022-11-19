from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, F, Case, When, Avg
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Subcategory, Rating
from .forms import ProductForm

import operator


def get_avg_rating(product_id):
    product = get_object_or_404(Product, pk=product_id)
    ratings = product.ratings.all()
    avg_rating = ratings.aggregate(Avg('score'))['score__avg']
    if avg_rating is None:
        avg_rating = 0
    avg_rating = round(avg_rating)
    return avg_rating


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
    all_subcategories = Subcategory.objects.all()
    subcategories = all_subcategories
    selected_category = None
    selected_subcategory = None
    favorites = request.session.get('favorites', [])
    page_number = 1
    query = None
    direction = None

    if request.GET:
        page_number = request.GET.get('page')

        # sorting functions
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'price':
                sortkey = 'sort_price'
                products = products.annotate(
                    sort_price=Case(
                        When(on_sale=False, then=F('price')),
                        When(on_sale=True, then=(F('price') - F('discount') *
                                                 F('price') / 100)),
                    ),
                )
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # category and subcategory filters
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

        # favorite filter
        if 'favorites' in request.GET:
            products = products.filter(id__in=favorites)

        # indoor filter
        if 'indoors' in request.GET:
            products = products.filter(indoors=True)

        # bargain filter
        if 'bargains' in request.GET:
            products = products.filter(on_sale=True)

        # search filter
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    for sc in all_subcategories:
        if sc.name == 'various_veg':
            sc.index = 1
        else:
            sc.index = 0
    all_subcategories = sorted(
        all_subcategories, key=operator.attrgetter('index'))
    for sc in subcategories:
        if sc.name == 'various_veg':
            sc.index = 1
        else:
            sc.index = 0
    subcategories = sorted(
        subcategories, key=operator.attrgetter('index'))

    # add on sale price attribute to products on sale
    for product in products:
        if product.on_sale:
            product.on_sale_price = \
                round(product.price-product.discount*product.price/100, 2)

    # add avg rating attribute to products
    for product in products:
        product.avg_rating = get_avg_rating(product.id)

    paginator = Paginator(products, 20, orphans=3)
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
        'all_subcategories': all_subcategories,
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

    product.avg_rating = get_avg_rating(product.id)
    product.num_rating = product.ratings.all().count()

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def rate_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if request.method == 'POST':
        redirect_url = request.POST.get('redirect_url')

        if not user.is_authenticated:
            messages.info(
                request, 'You need to be logged in to rate a product.')
            return redirect(redirect_url)

        if product.ratings.all().filter(rater=user.profile).exists():
            messages.info(
                request, 'You have already rated this product.')
            return redirect(redirect_url)

        score = request.POST.get('score')
        rating = Rating(score=score, rater=user.profile, product=product)
        rating.save()
        messages.success(
            request, f'Your rating of {product.name} was successfully saved!')

    return redirect(redirect_url)


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
