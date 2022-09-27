from django.shortcuts import redirect


def adjust_favorites(request, product_id):
    """
    Add or delete a product in the users favorite list
    """
    product = int(product_id)
    favorites = request.session.get('favorites', [])
    redirect_url = request.POST.get('redirect_url')

    if product in favorites:
        favorites.remove(product)
    else:
        favorites.append(product)

    request.session['favorites'] = favorites

    return redirect(redirect_url)
