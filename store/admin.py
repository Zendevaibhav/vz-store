
# from import_export.admin import ImportExportModelAdmin

# @admin.register(Category)
# class CategoryAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'parent')

# @admin.register(Product)
# class ProductAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'category', 'price')

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Category, Product , Store

# Optional: register models
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Store)

# Customize the admin header
admin.site.site_header = "WELCOME TO VZ Store ADMIN PAGE"
admin.site.site_title = "VZ Store Admin Portal"
admin.site.index_title = format_html(
    'Welcome to VZ Store. <a href="{}">Back to Main Page</a>',
    reverse('home')  # This generates the URL for the front-end home page
)
