from django.urls import path

from .views import (
    HomeProductsView,
    ProductView,
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
)


urlpatterns = [
    # path('', HomeProductsView.as_view(), name='home-page'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    # At the end, a slash is usually put, but according to the test it should be done like this
    path('item/<int:pk>', ProductView.as_view(), name='detail-product'),
    path('buy/<int:pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

]
