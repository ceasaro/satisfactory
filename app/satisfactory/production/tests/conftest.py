import pytest

from satisfactory.production.models import Product, Factory


@pytest.fixture
def iron():
    product, _ = Product.get_or_create_product('Iron', 'Fe', 30)
    return product


@pytest.fixture
def pipe(iron):
    product, _ = Product.get_or_create_product('Iron pipe', 'Fe-pipe', 15, [('Fe', 15)])
    return product


@pytest.fixture
def screw(pipe):
    product, _ = Product.get_or_create_product('Screw', 'screw', 40, [('Fe-pipe', 10)])
    return product


@pytest.fixture
def iron_plate(iron):
    product, _ = Product.get_or_create_product('Iron plate', 'Fe-plate', 20, [('Fe', 30)])
    return product


@pytest.fixture
def reinforced_plate(iron_plate, screw):
    product, _ = Product.get_or_create_product('Reinforced plate', 'Fe-rplate', 5, [('screw', 60), ('Fe-plate', 20)])
    return product


@pytest.fixture
def modular_frame(reinforced_plate, screw):
    product, _ = Product.get_or_create_product('Modular frame', 'modular_frame', 5, [('screw', 140), ('Fe-rplate', 7.5)])
    return product
