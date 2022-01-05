from django.urls import path
from django.views.generic import TemplateView

app_name = 'production'

urlpatterns = [
    path('products', TemplateView.as_view(template_name='production/products.html'), name='products'),
]
