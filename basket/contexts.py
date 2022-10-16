from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.on_sale:
            product.on_sale_price = \
                round(product.price-product.discount*product.price/100, 2)
            subtotal = quantity * product.on_sale_price
        else:
            subtotal = quantity * product.price
        total += subtotal
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    delivery = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100) * total

    if basket_items:
        if delivery < settings.MINIMUM_DELIVERY_COST:
            delivery = settings.MINIMUM_DELIVERY_COST

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
