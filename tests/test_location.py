import pytest

from guitarpickspy.location import Location

def test_init():
    pkv = Location("Pikeville", "KY")
    assert isinstance(pkv, Location)

@pytest.fixture
def cities():
    pkv1 = Location("Pikeville", "KY")
    pkv2 = Location("Pikeville", "KY")
    pkv3 = Location("Pikeville", "TN")
    nashville = Location("Nashville", "TN")
    return [pkv1, pkv2, pkv3, nashville]

def test_str(cities):
    computed = [str(city) for city in cities]
    expected = ["Pikeville, KY",
                "Pikeville, KY",
                "Pikeville, TN",
                "Nashville, TN"]
    assert computed == expected

def test_eq(cities):
    assert cities[0] == cities[1]
    assert not cities[1] == cities[2]
    assert not cities[2] == cities[3]
    assert not cities[1] == cities[3]


def test_ne(cities):
    assert not cities[0] != cities[1]
    assert cities[1] != cities[2]
    assert cities[2] != cities[3]
    assert cities[1] != cities[3]

def test_lt(cities):
    assert not cities[0] < cities[1]
    assert cities[3] < cities[0]
    assert cities[1] < cities[2]

def test_le(cities):
    assert cities[0] <= cities[1]
    assert cities[3] <= cities[0]
    assert cities[1] <= cities[2]


def test_gt(cities):
    assert not cities[1] > cities[0]
    assert cities[0] > cities[3]
    assert cities[2] > cities[1]

def test_ge(cities):
    assert  cities[1] >= cities[0]
    assert cities[0] >= cities[3]
    assert cities[2] >= cities[1]
