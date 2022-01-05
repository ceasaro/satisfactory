from django.urls import path

from satisfactory.production.views import ProductsView

app_name = 'production'

urlpatterns = [
    path('products', ProductsView.as_view(template_name='production/products.html'), name='products'),
]
