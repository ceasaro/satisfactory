from decimal import Decimal

from satisfactory.production.models import Product
from anytree import Node


def get_resource_data(product):
    assert isinstance(product, Product)
    resource_list = {}
    produced_product = product.get_produced()
    node = Node(create_product_dict(produced_product.product, produced_product.amount))

    def _get_resource_tree(_product, parent_node, factor):
        for resource in _product.factory.resources.all():
            required = resource.amount * factor
            produced_resource = resource.resource.get_produced()
            resource_list.setdefault(resource.resource.code, 0)
            resource_list[resource.resource.code] += required

            _get_resource_tree(resource.resource,
                               Node(create_product_dict(resource.resource, required), parent=parent_node),
                               factor=Decimal(required / produced_resource.amount),
                               )
        return parent_node

    return _get_resource_tree(product, node, factor=Decimal(1.0)), resource_list


def create_product_dict(product, amount):
    return {
        'product': product,
        'amount': amount
    }
