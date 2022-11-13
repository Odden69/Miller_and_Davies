from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/checkout_success/<order_number>', views.checkout_success,
         name='checkout_success'),
    path('checkout/cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('checkout/wh/', webhook, name='webhook'),
]
