from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse




# Main page
def main_page(request):
    return render(request, 'store/main_page.html')

# Home page
def home(request):
    return HttpResponse("Welcome to Home Page")

def home(request):
    return render(request, 'store/home.html')

# Categories page
def categories(request):
    return render(request, 'store/categories.html')

def categories_list(request):
    categories = Category.objects.filter(parent=None)  # main categories
    return render(request, 'store/categories.html', {'categories': categories})

# Products page
def products(request):
    return render(request, 'store/products.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})



