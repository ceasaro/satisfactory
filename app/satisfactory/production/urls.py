from django.urls import path

from satisfactory.production.views import ProductsView, ProductAddView, ProductAddSuccessView, ProductDeleteView, \
    ProductDetailView

app_name = 'production'

urlpatterns = [
    path('products', ProductsView.as_view(), name='products'),
    path('products/<product_code>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', ProductAddView.as_view(), name='add-product'),
    path('products/add/success', ProductAddSuccessView.as_view(), name='add-product-success'),
    path('products/<pk>/delete/', ProductDeleteView.as_view(), name='delete-product'),
]
