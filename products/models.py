from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from profiles.models import Profile


def get_sentinel_category():
    return Category.objects.get_or_create(name='deleted_category')[0]


def get_sentinel_subcategory():
    return Subcategory.objects.get_or_create(name='deleted_subcategory')[0]


class Season(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET(get_sentinel_category),
                                 related_name='subcategories')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.SET(
                                        get_sentinel_subcategory))
    sawing_times = models.ManyToManyField(Season,
                                          related_name='products_to_saw')
    harvest_times = models.ManyToManyField(Season,
                                           related_name='products_to_harvest')
    indoors = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False, null=False, blank=False)
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

    class Meta:
        ordering = ('name',)


class Rating(models.Model):

    SCORES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    score = models.IntegerField(default=0, choices=SCORES)
    rater = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ratings')
