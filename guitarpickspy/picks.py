"""Classes used to keep track of a guitar pick populate_collection

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
"""

from guitarpickspy.location import Location
import pickle

def str2bool(v):
    """Function to return True if given a string argument 'True'
    (Lifted off the Interent, I forgot from whom)
    """
    return v == 'True'



class GuitarPick:
    """a super class for various categories of guitar picks

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
        matches(field, value) -> boolean
            returns True if the pick's 'field' is 'value'
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
#        return 'A ' + self.color + ' pick that says ' + self.name
        return f"A {self.color} pick that says {self.name}"

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

    def matches(self, field, value):
        """returns True if the pick's 'field' is 'value'

        This method returns true if the object's property
        specified by 'field' has the value specified by 'value'.
        It is used in search methods
        """
        return ((field == 'name' and self.name == value) or
            (field == 'color' and self.color == value))

    def file_str(self):
#        return '%s,%s' % (self.name, self.color)
        return f"{self.name},{self.color}"

class SouvenirPick(GuitarPick):
    def __init__(self, name, location, year, color, isFunctional):
        super().__init__(name, color)
        self.location = location
        self.year = year
        self.isFunctional = isFunctional

    def __str__(self):
#        return ('A %s pick that says %s from %s in %d.' %
#            (self.color, self.name, str(self.location), self.year))
        return (f"A {self.color} pick that says '{self.name}' " +
                f"from {self.location} in {self.year}")


    def matches(self, field, value):
        """returns True if the picks 'field' is 'value'

        This method returns true if the object's property
        specified by 'field' has the value specified by 'value'.
        It is used in search methods
        """
        return ((super().matches(field, value)) or
            (field == 'location' and self.location == value) or
            (field == 'year' and self.year == value) or
            (field == 'isFunctional' and self.isFunctional == value))

    def print_details(self):
        """print the full details of the pick

        This method displays, one line at a time, each attribute
        of this guitar pick
        """
        # print('Name: ' + self.name)
        # print('From: ' + str(self.location))
        # print('Color(s): + ' + self.color)
        # if self.isFunctional:
        #     print('is a real pick')
        # else:
        #     print('is a novelty pick')
        # print('Year obtained: ' + str(self.year))
        print(f"Name: {self.name}")
        print(f"From: {self.location}")
        print(f"Color(s): {self.color}")
        if self.isFunctional:
            print("is a real pick")
        else:
            print("is a novelty pick")
        print(f"Year obtained: {self.year}")

    def file_str(self):
#        return '%s,%s,%s,%s,%d,%s' % (
        return (f"{self.name},{self.color},{self.location.city}," +
                f"{self.location.state},{self.year},{self.isFunctional}")

class PlayingPick(GuitarPick):
    """a pick that is actually used for playing a guitar

    This class will represent picks in a collection which are
    actually used for playing a guitar

    (Expected) Attributes
    ---------------------
        thickness: float
            the thickness of the pick in mm
        quantity: int
            the number of this type of pick owned
    """
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
        matching_picks = [pick for pick in self.picks if pick.matches(field,value)]
        # matching_picks = []
        # for pick in self.picks:
        #     if pick.matches(field, value):
        #         matching_picks.append(pick)
        return matching_picks

    def write_csv(self, filename):
        """Write the contents of the collection to a text file
        """
        try:
            fout = open(filename, 'w')
            for pick in self.picks:
                fout.write(pick.file_str() + '\n')
            fout.close()
        except:
#            print('Error writing to file: %s' % filename)
            print(f"Error writing to file {filename}")


    def read_csv(self, filename):
        """adds records from a CSV file into the collection

        This method is based on work by BlueJ
        Currently this method only works for adding SouvenirPick objects
        """
        NAME = 0
        COLOR = 1
        CITY = 2
        STATE = 3
        YEAR = 4
        FUNCTIONAL = 5
        try:
            fin = open(filename, 'r')
            for line in fin:
                if len(line) > 0 and line[0] != '#':
                    parts = line[:-1].split(',')
                    name = parts[NAME]
                    color = parts[COLOR]
                    city = parts[CITY]
                    state = parts[STATE]
                    year = int(parts[YEAR])
                    isFunctional = str2bool(parts[FUNCTIONAL])
                    self.picks.append(SouvenirPick(
                        name,
                        Location(city, state),
                        year,
                        color,
                        isFunctional))
        except FileNotFoundError:
#            print('No such file: %s' % filename)
            print(f"No such file: {filename}")
        except ValueError:
#            print('%s does not have proper format' % filename)
            print(f"{filename} does not have proper format")

    def save(self, filename):
        """This method will save the collection as a single data file
        """
        try:
            fout = open(filename, 'wb')
            pickle.dump(self, fout)
            fout.close()
        except Exception as error:
#            print('Error saving to file: %s' % filename)
#            print('Error reported: %s', error)
            print(f"Error saving to file: {filename}")
            print(f"Error reported as {error}")

    def open(self, filename):
        """This method will open a file storing a collection
        """
        try:
            fin = open(filename, 'rb')
            new_picks = pickle.load(fin)
            assert isinstance(new_picks, GuitarPickCollection)
            self.picks = new_picks.picks
        except FileNotFoundError:
#            print('No such file: %s' % filename)
            print(f"No such file as {filename}")
        except (AssertionError, pickle.UnpicklingError):
#            print('%s not a guitar pick collection file' % filename)
            print(f"{filename} is not a guitar pick collection file")

    def _populate_collection(self):
        self.picks.append(SouvenirPick("Nashville",
                Location("Nashville", "TN"),
                2018, "purple", True))
        self.picks.append(SouvenirPick("Nashville",
                Location("Nashville", "TN"),
                2018, "orange", True))
        self.picks.append(SouvenirPick("Memphis",
                Location("Memphis", "TN"),
                2017, "purple", True))
        self.picks.append(SouvenirPick("Memphis",
                Location("Memphis", "TN"),
                2017, "orange", True))
        self.picks.append(SouvenirPick("Cooter's Garage",
                Location("Gatlinburg", "TN"),
                2019, "purple", True))
        self.picks.append(SouvenirPick("Cooter's Garage",
                Location("Gatlinburg", "TN"),
                2019, "orange", True))
        self.picks.append(SouvenirPick("Mothman Search Team",
                Location("Point Pleasant", "WV"),
                2017, "black", True))
        self.picks.append(SouvenirPick("Mothman Search Team",
                Location("Point Pleasant", "WV"),
                2017, "green", True))
        self.picks.append(SouvenirPick("JWT School of Rock",
                Location("Pikeville", "KY"),
                2016, "black", True))

def tryit():
    collection = GuitarPickCollection()
    collection._populate_collection()
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

    # for pick in collection.picks:
    #     print(pick.file_str())

    collection.write_csv('picks.csv')
    collection.save('picks.gpc')

def try_open():
    collection = GuitarPickCollection()
#    collection.open('picks.csv')
    collection.open('picks.gpc')
    collection.list_all()
    for pick in collection.picks:
        print(pick)

def try_read():
    collection = GuitarPickCollection()
    collection.read_csv('picks.csv')
    collection.list_all()

if __name__ == '__main__':
    tryit()
#    try_open()
#    try_read()
