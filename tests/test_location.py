import pytest

from guitarpickspy.location import Location

def test_constructor():
    pkv = Location("Pikeville", "KY")
    assert isinstance(pkv, Location)

# more to come
