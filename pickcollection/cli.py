# This is a command line interface for the GuitarPickCollection class
# It borrows heavily from code done in the BlueJ book
# by David J. Barnes and Michael Kölling.

from location import Location
from picks import GuitarPick, SouvenirPick, GuitarPickCollection


class CommandWords:
    valid_command = ['list', 'search', 'add', 'help', 'quit']

    @classmethod
    def is_command(cls, a_string):
        if not (a_string is None):
            for command in valid_command:
                if command == a_string:
                    return True
        return False

    @classmethod
    def get_all(cls):
        ret_str = ""
        for command in valid_command:
            ret_str += command
        return ret_str


class Parser:
    def get_command():
        '''Read the next command from the user.
        The returned command will be valid.

        returns: a valid command
        '''
        command = ''
        do = True
        while do:
            word = input('> ').strip().lower()
            if (CommandWords.is_command(word)):
                command = word
            else:
                print('Unrecognized command: ' + word)
                print('Valid commands are: ' + CommandWords.get_all())
            do = (command == '')
        return commmand
