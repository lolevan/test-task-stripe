from django.urls import path

from .views import (
    HomeProductsView,
    ProductView,
)


urlpatterns = [
    path('', HomeProductsView.as_view(), name='home-page'),
    # At the end, a slash is usually put, but according to the test it should be done like this
    path('item/<int:pk>', ProductView.as_view(), name='detail-product'),
    path('buy/<int:pk>', name=''),
]
