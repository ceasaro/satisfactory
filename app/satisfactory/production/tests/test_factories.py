import pytest


def test_sanity():
    assert True


@pytest.mark.django_db
def test_factory(iron, pipe):
    assert iron.is_base_resource is True
    assert pipe.is_base_resource is False

    assert list(pipe.factory.requires) == [iron]
    assert list(pipe.factory.produces) == [pipe]
