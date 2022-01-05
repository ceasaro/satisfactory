from django.views.generic import TemplateView

from satisfactory.production.models import Product


class ProductsView(TemplateView):
    template_name = 'production/products.html'

    def get_context_data(self, **kwargs):
        return {'products': Product.objects.all()}
