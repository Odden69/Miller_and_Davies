from django.urls import path
from . import views

urlpatterns = [
    path('favorites/adjust/<product_id>', views.adjust_favorites,
         name='adjust_favorites'),
]
