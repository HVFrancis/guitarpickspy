# This module contains a class to represent a place
# Usually a City and and State, but any two descriptors
# for the location can be used


class Location:
    '''A location represents a place, usually
    a city and a state
    '''
    def __init__(self, city, state):
        '''Initialize an object of class Location

        Parameters:
            city (str) - the city of the location
            state (str) - the state (but could be country, etc)
        '''
        self.city = city
        self.state = state

    def __str__(self):
        return self.city + ', ' + self.state

    def __eq__(self, other):
        if self is other:
            return true
        elif not isinstance(other, Location):
            return false
        else:
            return (self.city == other.city and
                    self.state == other.state)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        '''Locations are ordered alphabetically by city, then state'''
        if self.city == other.city:
            return self.state < other.state
        else:
            return self.city < other.city

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
