import pytest


def test_sanity():
    assert True


@pytest.mark.django_db
def test_factory(iron, pipe):
    assert iron.is_base_resource is True
    assert pipe.is_base_resource is False

    assert list(pipe.factory.requires) == [iron]
    assert list(pipe.factory.produces) == [pipe]


@pytest.mark.django_db
def test_required_resources(iron, pipe, screw, iron_plate, reinforced_plate, modular_frame):
    assert list(iron.resources) == []
    assert list(pipe.resources) == [iron]
    assert modular_frame.resources == {iron, pipe, screw, iron_plate, reinforced_plate}
    assert modular_frame.required_base_products == {iron}, "Only iron is a base product for a modular frame"

