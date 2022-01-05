from decimal import Decimal

from satisfactory.production.models import Product
from anytree import Node


def get_resource_tree(product, parent_node=None, factor=Decimal(1.0)):
    produced_product = product.get_produced()
    if parent_node is None:
        parent_node = Node(create_product_dict(produced_product.product, produced_product.amount))
    assert isinstance(product, Product)
    for resource in product.factory.resources.all():
        required = resource.amount * factor
        produced_resource = resource.resource.get_produced()
        get_resource_tree(resource.resource,
                          Node(create_product_dict(resource.resource, required), parent=parent_node),
                          factor=Decimal(required / produced_resource.amount),
                          )
    return parent_node


def create_product_dict(product, amount):
    return {
        'product': product,
        'amount': amount
    }
