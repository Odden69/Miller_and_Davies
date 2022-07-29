from django.shortcuts import render, redirect


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

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_quantity_in_basket(request, item_id):
    """
    Adjust the quantity for a selected product in the basket
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    basket[item_id] = quantity
    request.session['basket'] = basket
    print(basket)

    return redirect(redirect_url)
