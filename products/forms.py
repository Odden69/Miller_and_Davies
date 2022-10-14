from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Subcategory, Season


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subcategories = Subcategory.objects.all()
        s_friendly_names = [(s.id, s.friendly_name)
                            for s in subcategories]
        seasons = Season.objects.all()
        saw_friendly_names = [(s.id, s.friendly_name)
                              for s in seasons]
        harv_friendly_names = [(s.id, s.friendly_name)
                               for s in seasons]

        self.fields['subcategory'].choices = s_friendly_names
        self.fields['sawing_times'].choices = saw_friendly_names
        self.fields['harvest_times'].choices = harv_friendly_names
        self.fields['sawing_times'].label = 'Sawing Times'
        self.fields['harvest_times'].label = 'Harvest/Flowering Times'
