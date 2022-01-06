from django import forms
from django.core.exceptions import ValidationError

from satisfactory.production.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(help_text='A name for your product.')
    code = forms.CharField(help_text='A unique code for your product.')
    production_amount = forms.IntegerField(help_text='The production amount of this product in a factory.')

    def __init__(self, **kwargs):
        self.request = kwargs.pop('request')
        self.resources = []
        super().__init__(**kwargs)

    def clean(self):
        super().clean()
        for resource in self.request.POST.getlist('resources', []):
            if resource:
                resource_parts = resource.split(';')
                resource_code = resource_parts[0]
                try:
                    Product.objects.get(code=resource_code)
                except Product.DoesNotExist as e:
                    raise ValidationError(f"Unknown product code '{resource_code}'", code='unknown_product_code')
                if len(resource_parts) == 1:
                    raise ValidationError(f"Amount is needed for product code '{resource_code}'",
                                          code='unknown_product_amount')
                try:
                    amount = float(resource_parts[1])
                except (ValueError, TypeError):
                    raise ValidationError(f'Amount ({resource_parts[1]}) must be valid number',
                                          code='invalid_product_amount')
                self.resources.append((resource_code, amount))
