from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def basket(request):
    """ Returns the shopping basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a product to the shopping basket (with a selected quantity)
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Product, pk=item_id)

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated the quantity of \
            {product.name}s to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} was added to your basket')

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_quantity_in_basket(request, item_id):
    """
    Adjust the quantity for a selected product in the basket
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Product, pk=item_id)

    basket[item_id] = quantity
    messages.success(request, f'Updated {product.name} quantity to \
        {basket[item_id]}')
    request.session['basket'] = basket

    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """
    Remove a selected product from the basket
    """
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    product = get_object_or_404(Product, pk=item_id)

    try:
        basket.pop(item_id)
        messages.success(
            request, f'{product.name} was deleted from your basket')

        request.session['basket'] = basket
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return redirect(redirect_url)
