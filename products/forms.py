from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Subcategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['sku', 'name', 'price', 'size', 'description', 'image',
                  'subcategory', 'on_sale', 'discount']

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subcategories = Subcategory.objects.all()
        s_friendly_names = [(s.id, s.friendly_name)
                            for s in subcategories]

        self.fields['subcategory'].choices = s_friendly_names
