from anytree import RenderTree, render
from django.core.management.base import BaseCommand

from satisfactory.production.models import Product, Resource, ProducedProduct
from satisfactory.production.product_helper import get_resource_tree


class Command(BaseCommand):
    help = 'Creates / updates products'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--product-code', required=True, type=str)

    def handle(self, *args, product_code, **options):
        product = Product.objects.get(code=product_code)
        resource_list = {}
        print(f"\nResource tree: {product}\n")
        tree = get_resource_tree(product)
        RenderTree(tree, style=render.ContStyle)
        for pre, _, node in RenderTree(tree):
            product = node.name.get('product')
            amount = node.name.get('amount')
            print(f"{pre}{product.name} ({amount:.2f})")
            resource_list.setdefault(product.code, 0)
            resource_list[product.code] += amount

        print("\n\nTOTAL:\n")
        for resource, amount in resource_list.items():
            print(f"{resource}: {amount:.2f}")
        print("\n\n")
