from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView

from satisfactory.production.forms import ProductForm
from satisfactory.production.models import Product


class ProductsView(TemplateView):
    template_name = 'production/products.html'

    def get_page_message(self):
        return ''

    def get_context_data(self, **kwargs):
        return {'products': Product.objects.all(), 'message': self.get_page_message()}


class ProductAddView(FormView):
    template_name = 'production/product-add.html'
    form_class = ProductForm

    def form_valid(self, form):
        data = form.cleaned_data
        product, created = Product.get_or_create_product(data.get('name'), data.get('code'), data.get('production_amount'))
        return HttpResponseRedirect(f'add/success?name={product.name}{"&created" if created else ""}')


class ProductAddSuccessView(ProductsView):
    template_name = 'production/products.html'

    def get_page_message(self):
        get_data = self.request.GET
        return f"Successfully {'created' if get_data.get('created') else 'updated'} product {get_data.get('name')}"
