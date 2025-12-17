import csv
from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Import products from CSV'

    def handle(self, *args, **kwargs):
        with open('products.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # main category
                main_category, _ = Category.objects.get_or_create(
                    name=row['category'],
                    parent=None
                )

                # subcategory
                sub_category, _ = Category.objects.get_or_create(
                    name=row['subcategory'],
                    parent=main_category
                )

                # product
                Product.objects.create(
                    name=row['name'],
                    price=row['price'],
                    category=sub_category,
                    description=row['description']
                )

        self.stdout.write(self.style.SUCCESS('Products imported successfully'))
