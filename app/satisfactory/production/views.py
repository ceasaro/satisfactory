from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, DeleteView

from satisfactory.production.forms import ProductForm
from satisfactory.production.models import Product
from satisfactory.production.product_helper import get_resource_data


class ProductsView(TemplateView):
    template_name = 'production/products.html'

    def get_page_message(self):
        return ''

    def get_context_data(self, **kwargs):
        return {'products': Product.objects.all(), 'message': self.get_page_message()}


class ProductDetailView(ProductsView):

    def __init__(self, *args, **kwargs):
        self.product = None
        super().__init__(*args, **kwargs)

    def get(self, request, product_code, **kwargs):
        self.product = Product.objects.get(code=product_code)
        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):
        product_tree, product_resources = get_resource_data(self.product)
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        context['product_tree'] = product_tree
        context['product_resources'] = product_resources
        return context


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('production:products')


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
