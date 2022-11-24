from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
# _ becomes an alias for gettext_lazy

# This code was copied as a whole from the boutique ado project


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/\
custom_clearable_file_input.html'
