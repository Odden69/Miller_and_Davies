from django.contrib import admin
from .models import Product, Category, Subcategory

adminFields = [Product, Category, Subcategory]

admin.site.register(adminFields)