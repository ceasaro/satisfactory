import pytest

from satisfactory.production.models import Product, Factory


@pytest.fixture
def iron():
    iron = Product.objects.create(name='Iron', code='Fe')
    iron_factory = Factory.objects.create()
    iron_factory.add_product(product=iron, amount=30)
    return iron


@pytest.fixture
def pipe(iron):
    pipe = Product.objects.create(name='Iron pipe', code='Fe-pipe')
    pipe_factory = Factory.objects.create()
    pipe_factory.add_resource(resource=iron, amount=15)
    pipe_factory.add_product(product=pipe, amount=15)
    return pipe
