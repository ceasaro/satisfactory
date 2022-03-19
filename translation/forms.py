from django import forms


class TranslateForm(forms.Form):
    original = forms.Textarea()
    translated = forms.Textarea()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
