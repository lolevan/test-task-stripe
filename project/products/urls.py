from django.urls import path

from .views import (
    HomeProductsView,
)


urlpatterns = [
    path('', HomeProductsView.as_view(), name='home-page'),

]
