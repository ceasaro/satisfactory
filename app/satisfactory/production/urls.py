from django.urls import path

from satisfactory.production.views import ProductsView, ProductAddView, ProductAddSuccessView

app_name = 'production'

urlpatterns = [
    path('products', ProductsView.as_view(), name='products'),
    path('products/add', ProductAddView.as_view(), name='add-product'),
    path('products/add/success', ProductAddSuccessView.as_view(), name='add-product-success'),
]
