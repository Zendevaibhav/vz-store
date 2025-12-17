from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'parent')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'price')
