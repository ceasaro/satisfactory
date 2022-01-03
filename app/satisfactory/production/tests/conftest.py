import pytest

from satisfactory.production.models import Product, Factory


@pytest.fixture
def iron():
    return Product.get_or_create_product('Iron', 'Fe', 30)


@pytest.fixture
def pipe(iron):
    return Product.get_or_create_product('Iron pipe', 'Fe-pipe', 15, [('Fe', 15)])


@pytest.fixture
def screw(pipe):
    return Product.get_or_create_product('Screw', 'screw', 40, [('Fe-pipe', 10)])


@pytest.fixture
def iron_plate(iron):
    return Product.get_or_create_product('Iron plate', 'Fe-plate', 20, [('Fe', 30)])


@pytest.fixture
def reinforced_plate(iron_plate, screw):
    return Product.get_or_create_product('Reinforced plate', 'Fe-rplate', 5, [('screw', 60), ('Fe-plate', 20)])


@pytest.fixture
def modular_frame(reinforced_plate, screw):
    return Product.get_or_create_product('Modular frame', 'modular_frame', 5, [('screw', 140), ('Fe-rplate', 7.5)])
