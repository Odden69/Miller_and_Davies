from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def adjust_favorites(request, product_id):
    """
    Add or delete a product in the users favorite list

    """
    product_id = int(product_id)
    favorites = request.session.get('favorites', [])
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=product_id)

    if product_id in favorites:
        favorites.remove(product_id)
        messages.info(
            request, f'{product.name} was removed from your favorites')
    else:
        favorites.append(product_id)
        messages.info(
            request, f'{product.name} was added to your favorites')

    request.session['favorites'] = favorites

    return redirect(redirect_url)
