from django.views import View
from django.views.generic import ListView

from .models import Item


class HomeProductsView(ListView):
    model = Item
    template_name = 'products/home.html'
    context_object_name = 'products'

