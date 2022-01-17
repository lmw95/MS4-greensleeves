from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name',
                  'email',
                  'phone_number',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'postcode',
                  'country',
                )
    
    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated labels
           and set auto-focus on first field"""

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email',
            'phone_number': 'Phone / mobile number',
            'street_address1': 'Address line 1',
            'street_address2': 'Address line 2',
            'town_or_city': 'Town / city',
            'county': 'County',
            'postcode': 'Postcode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False