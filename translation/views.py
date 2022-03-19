from django.urls import reverse_lazy
from django.views.generic import FormView

from translation.forms import TranslateForm


class TranslateView(FormView):
    template_name = 'translation/translate.html'
    form_class = TranslateForm
    success_url = reverse_lazy("translation:home")

    def get_page_message(self):
        return 'Joehoe'

    def get_context_data(self, **kwargs):
        return {}

