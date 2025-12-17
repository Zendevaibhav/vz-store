# from django.urls import path
# from .views import product_list, home

# urlpatterns = [
#     path('', home, name='home'),  # Home page
#     path('products/', product_list, name='product_list'),  # Products page
# ]
# 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('categories/', views.categories_list, name='categories_list'),
    path('products/', views.products_list, name='products_list'),
]
