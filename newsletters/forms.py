from django import forms
from .models import NewsletterSubscriber


class NewsletterSignupForm(forms.ModelForm):
    """
    Lets the user sign up for a newsletter
    """

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = "example@email.com"
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False
