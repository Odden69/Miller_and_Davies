from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def get_sentinel_category():
    return Category.objects.get_or_create(name='deleted_category')[0]


def get_sentinel_subcategory():
    return Subcategory.objects.get_or_create(name='deleted_subcategory')[0]


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET(get_sentinel_category),
                                 related_name='subcategories')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.SET(
                                        get_sentinel_subcategory))
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    discount = models.IntegerField(default=0,
                                   validators=[
                                    MaxValueValidator(100),
                                    MinValueValidator(0)
                                   ])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField(default=0,
                               validators=[
                                MaxValueValidator(5000),
                                MinValueValidator(0)
                               ])

    def __str__(self):
        return self.name
