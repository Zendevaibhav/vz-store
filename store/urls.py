from django.urls import path
from .views import product_list, home

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('products/', product_list, name='product_list'),  # Products page
]
