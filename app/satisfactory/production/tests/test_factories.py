from datetime import timedelta

import pytest

from satisfactory.production.models import Factory, Resource


def test_sanity():
    assert True


@pytest.mark.django_db
def test_factory():
    iron = Resource.objects.create(name='Iron', code='Fe')
    iron_factory = Factory.objects.create(produces=iron, amount=30, production_time=timedelta(minutes=1))
    print(iron)
    print(iron_factory)