from django.views import View
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import JsonResponse

import stripe

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductView(DetailView):
    model = Item
    template_name = 'products/product_item.html'
    context_object_name = 'product_item'


class HomeProductsView(ListView):
    model = Item
    template_name = 'products/home.html'
    context_object_name = 'products'


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        product = Item.objects.get(pk=product_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': product.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )

        return JsonResponse({'id': session.id})
