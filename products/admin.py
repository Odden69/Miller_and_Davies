from django.contrib import admin
from .models import Product, Category, Subcategory, Season, Rating

adminFields = [Product, Category, Subcategory, Season, Rating]


admin.site.register(adminFields)
