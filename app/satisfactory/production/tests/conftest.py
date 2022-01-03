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


@pytest.fixture
def screw(pipe):
    screw = Product.objects.create(name='Screw', code='screw')
    factory = Factory.objects.create()
    factory.add_resource(resource=pipe, amount=10)
    factory.add_product(product=screw, amount=40)
    return screw


@pytest.fixture
def iron_plate(iron):
    iron_plate = Product.objects.create(name="Iron plate", code="Fe-plate")
    factory = Factory.objects.create()
    factory.add_resource(resource=iron, amount=30)
    factory.add_product(product=iron_plate, amount=20)
    return iron_plate


@pytest.fixture
def reinforced_plate(iron_plate, screw):
    reinforced_plate = Product.objects.create(name="Reinforced plate", code="Fe-rplate")
    factory = Factory.objects.create()
    factory.add_resource(resource=iron_plate, amount=30)
    factory.add_resource(resource=screw, amount=60)
    factory.add_product(product=reinforced_plate, amount=5)
    return reinforced_plate


@pytest.fixture
def modular_frame(reinforced_plate, screw):
    modular_frame = Product.objects.create(name="Modular frame", code="modular_frame")
    factory = Factory.objects.create()
    factory.add_resource(resource=reinforced_plate, amount=7.5)
    factory.add_resource(resource=screw, amount=140)
    factory.add_product(product=modular_frame, amount=5)
    return modular_frame
