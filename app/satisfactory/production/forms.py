from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(help_text='A name for your product.')
    code = forms.CharField(help_text='A unique code for your product.')
    production_amount = forms.IntegerField(help_text='The production amount of this product in a factory.')

