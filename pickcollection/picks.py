# This module contains classes for maintaining a colleciton of
# Guitar Picks

from location import Location

class GuitarPick:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return 'A ' + self.color + ' pick that says ' + self.name

    def __eq__(self, other):
        if self is other:
            return true
        elif not isInstance(other, GuitarPick):
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
        '''This method returns true if the object's property
        specified by 'field' has the value specified by 'value'

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
        '''This method returns true if the object's property
        specified by 'field' has the value specified by 'value'

        '''
        return ((super().exists(field, value)) or
                (field == 'location' and self.location == value) or
                (field == 'year' and self.year == value) or
                (field == 'isFunctional' and isFunctional == value))
    
    def print_details(self):
        print('Name: ' + self.name)
        print('From: ' + str(self.location))
        print('Color(s): + ' + self.color)
        if self.isFunctional:
            print('is a real pick')
        else:
            print('is a novelty pick')
        print('Year obtained: ' + str(self.year))
    

class GuitarPickCollection:
    def __init__(self):
        self.picks = []
##        self.populate_collection()

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

     

        

    
    
