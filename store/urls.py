from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),       # Main page
    path('home/', views.home, name='home'),                 # Home page
    # path('admin/', admin.site.urls),       # Admin panel
    # path('', include('store.urls')),       # Front-end pages
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
]



