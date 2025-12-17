# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product

# def products_list(request):
#     products = Product.objects.all()
#     return render(request, 'store/products.html', {'products': products})


from django.shortcuts import render
from .models import Category, Product

# Home page
def home(request):
    return render(request, 'store/home.html')

# Categories page
def categories_list(request):
    categories = Category.objects.filter(parent=None)  # main categories
    return render(request, 'store/categories.html', {'categories': categories})

# Products page
def products_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})



