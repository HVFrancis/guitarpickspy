import pytest

#from guitarpickspy.location import Location
from guitarpickspy.picks import *
import pickle

def test_SouvenirPick_init():
    sp = SouvenirPick("Nashville",
        Location("Nashville", "TN"),
        2018, "purple", True)
    assert sp.name == "Nashville"
    assert sp.location == Location("Nashville", "TN")
    assert sp.year == 2018
    assert sp.color == "purple"
    assert sp.isFunctional == True

@pytest.fixture
def picks_collection():
    picks = []
    picks.append(SouvenirPick("Nashville",
            Location("Nashville", "TN"),
            2018, "purple", True))
    picks.append(SouvenirPick("Nashville",
            Location("Nashville", "TN"),
            2018, "orange", True))
    picks.append(SouvenirPick("Memphis",
            Location("Memphis", "TN"),
            2017, "purple", True))
    picks.append(SouvenirPick("Memphis",
            Location("Memphis", "TN"),
            2017, "orange", True))
    picks.append(SouvenirPick("Cooter's Garage",
            Location("Gatlinburg", "TN"),
            2019, "purple", True))
    picks.append(SouvenirPick("Cooter's Garage",
            Location("Gatlinburg", "TN"),
            2019, "orange", True))
    picks.append(SouvenirPick("Mothman Search Team",
            Location("Point Pleasant", "WV"),
            2017, "black", True))
    picks.append(SouvenirPick("Mothman Search Team",
            Location("Point Pleasant", "WV"),
            2017, "green", True))
    picks.append(SouvenirPick("JWT School of Rock",
            Location("Pikeville", "KY"),
            2016, "black", True))
    return picks;

def test_matches(picks_collection):
    assert picks_collection[0].matches('name', 'Nashville')
    assert picks_collection[0].matches('location',
                                        Location("Nashville", "TN"))
    assert picks_collection[0].matches('year', 2018)
    assert picks_collection[0].matches('color', 'purple')
    assert picks_collection[0].matches('isFunctional', True)
    assert not picks_collection[0].matches('color', 'orange')
    assert not picks_collection[0].matches('year', 2020)
    assert not picks_collection[0].matches('location',
                                        Location("Pikeville", "TN"))
