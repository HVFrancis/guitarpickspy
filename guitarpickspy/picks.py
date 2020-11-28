'''Classes used to keep track of a guitar pick populate_collection

This module contains the basic classes necessary to manage a
collection of guitar picks. These were first developed in Java
and are rewritten in Python as a way for the author to improve
his Python skills

Classes
-------
    GuitarPick
        a super class for two (so far) types of guitar picks
    SouvenirPick
        picks accumulated as a souvenir for travel or events
    PlayingPick
        picks that would actually be used for playing guitar
    GuitarPickCollection
        a class to manage a collection of picks
'''

from location import Location

class GuitarPick:
    '''a super class for various categories of guitar picks

    This class keeps track of the name (writing) of the pick
    and its primary color. Subclasses are expected to keep
    track of other properties.

    Attributes
    ----------
        name: str
            the name of the pick, usually any writing on it
        color: str
            the predominant color of the pick

    Methods
    -------
        exists(field, value) -> boolean
            returns True if the picks 'field' is 'value'
    '''
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return 'A ' + self.color + ' pick that says ' + self.name

    def __eq__(self, other):
        if self is other:
            return true
        elif not isinstance(other, GuitarPick):
            return false
        else:
            return (self.name == other.name and
                    self.color == other.color)

    def __lt__(self, other):
        if self.name.lower() == other.self.lower():
            return self.color < other.color
        else:
            return self.name < other.name

    def exists(self, field, value):
        '''returns True if the picks 'field' is 'value'

        This method returns true if the object's property
        specified by 'field' has the value specified by 'value'.
        It is used in search methods
        '''
        return ((field == 'name' and self.name == value) or
                (field == 'color' and self.color == value))


class SouvenirPick(GuitarPick):
    def __init__(self, name, location, year, color, isFunctional):
        super().__init__(name, color)
        self.location = location
        self.year = year
        self.isFunctional = isFunctional

    def __str__(self):
        return ('A %s pick that says %s from %s in %d.' %
                (self.color, self.name, str(self.location), self.year))

    def exists(self, field, value):
        '''returns True if the picks 'field' is 'value'

        This method returns true if the object's property
        specified by 'field' has the value specified by 'value'.
        It is used in search methods
        '''
        return ((super().exists(field, value)) or
                (field == 'location' and self.location == value) or
                (field == 'year' and self.year == value) or
                (field == 'isFunctional' and self.isFunctional == value))

    def print_details(self):
        print('Name: ' + self.name)
        print('From: ' + str(self.location))
        print('Color(s): + ' + self.color)
        if self.isFunctional:
            print('is a real pick')
        else:
            print('is a novelty pick')
        print('Year obtained: ' + str(self.year))


class PlayingPick(GuitarPick):
    '''a pick that is actually used for playing a guitar

    This class will represent picks in a collection which are
    actually used for playing a guitar

    (Expected) Attributes
    ---------------------
        thickness: float
            the thickness of the pick in mm
        quantity: int
            the number of this type of pick owned
    '''
    pass



class GuitarPickCollection:
    def __init__(self):
        self.picks = []

    def add_pick(self, pick):
        self.picks.append(pick)

    def list_all(self):
        for pick in self.picks:
            pick.print_details()
            print()

##    def search_by_name(self, name):
##        for pick in self.picks:
##            if pick.name == name:
##                print(pick)

    def search(self, field, value):
        matching_picks = []
        for pick in self.picks:
            if pick.exists(field, value):
                matching_picks.append(pick)
        return matching_picks

# I think these statements need to be reformated to fit into
# Python's 72-char limit (and related programming convensions)
    def populate_collection(self):
        self.picks.append(SouvenirPick("Nashville", Location("Nashville", "TN"),
                2018, "purple", True))
        self.picks.append(SouvenirPick("Nashville", Location("Nashville", "TN"),
                2018, "orange", True))
        self.picks.append(SouvenirPick("Memphis", Location("Memphis", "TN"),
                2017, "purple", True))
        self.picks.append(SouvenirPick("Memphis", Location("Memphis", "TN"),
                2017, "orange", True))
        self.picks.append(SouvenirPick("Cooter's Garage", Location("Gatlinburg", "TN"),
                2019, "purple", True))
        self.picks.append(SouvenirPick("Cooter's Garage", Location("Gatlinburg", "TN"),
                2019, "orange", True))
        self.picks.append(SouvenirPick("Mothman Search Team", Location("Point Pleasant", "WV"),
                2017, "black", True))
        self.picks.append(SouvenirPick("Mothman Search Team", Location("Point Pleasant", "WV"),
                2017, "green", True))
        self.picks.append(SouvenirPick("JWT School of Rock", Location("Pikeville", "KY"),
                2016, "black", True))


if __name__ == '__main__':
    collection = GuitarPickCollection()
    collection.populate_collection()
    collection.list_all()
    purple = collection.search('color', 'purple')
    for pick in purple:
        print(pick)

    in2017 = collection.search('year', 2017)
    for pick in in2017:
        print(pick)

    nashville = collection.search('location', Location('Nashville', 'TN'))
    for pick in nashville:
        print(pick)
