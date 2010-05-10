from django import forms
from ecomstore.catalog.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']

# vim: set ai ts=4 et sw=4 sts=4: 
