from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('basket/add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('basket/adjust/<item_id>', views.adjust_quantity_in_basket,
         name='adjust_quantity_in_basket'),
    path('basket/remove/<item_id>', views.remove_from_basket,
         name='remove_from_basket'),
]
