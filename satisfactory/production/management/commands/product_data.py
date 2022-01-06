from anytree import RenderTree, render
from django.core.management.base import BaseCommand

from satisfactory.production.models import Product
from satisfactory.production.product_helper import get_resource_data


class Command(BaseCommand):
    help = 'Creates / updates products'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--product-code', required=True, type=str)

    def handle(self, *args, product_code, **options):
        product = Product.objects.get(code=product_code)
        # resource_list = {}
        print(f"\nResource tree: {product}\n")
        tree, resource_list = get_resource_data(product)
        RenderTree(tree, style=render.ContStyle)
        for pre, _, node in RenderTree(tree):
            _product = node.name.get('product')
            amount = node.name.get('amount')
            print(f"{pre}{_product.name} ({amount:.2f})")

        print(f"\n\nTOTAL: {product}\n")
        for product_code, amount in resource_list.items():
            product = Product.objects.get(code=product_code)
            print(f"{product.name:<20}: {amount:.2f} (factories: {amount/product.get_produced().amount:.2f})")
        print("\n\n")
