from django.contrib import admin
from .models import Product, Category, Subcategory, Season

adminFields = [Product, Category, Subcategory, Season]

admin.site.register(adminFields)
