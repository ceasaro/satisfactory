from django.urls import path
from django.views.generic import TemplateView

from translation.views import TranslateView

app_name = 'translation'

urlpatterns = [
    path('', TemplateView.as_view(template_name='translation/home.html'), name='home'),
    path('translation', TranslateView.as_view(), name='translate'),
]
