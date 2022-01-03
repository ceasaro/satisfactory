from datetime import timedelta

import pytest

from satisfactory.production.models import Factory, Product, ProducedProducts


def test_sanity():
    assert True


@pytest.mark.django_db
def test_factory():
    iron = Product.objects.create(name='Iron', code='Fe')
    pipe = Product.objects.create(name='Iron pipe', code='Fe-pipe')
    iron_factory = Factory.objects.create()
    iron_factory.add_product(product=iron, amount=30)

    pipe_factory = Factory.objects.create()
    pipe_factory.add_resource(resource=iron, amount=15)
    pipe_factory.add_product(product=pipe, amount=15)

    assert iron_factory.produces == [iron]
    assert iron_factory.requires == []
    assert pipe_factory.produces == [pipe]
    assert pipe_factory.requires == [iron]

    assert iron.is_base_resource is True
    assert pipe.is_base_resource is False
