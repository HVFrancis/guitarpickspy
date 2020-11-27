# This is a command line interface for the GuitarPickCollection class
# It borrows heavily from code done in the BlueJ book
# by David J. Barnes and Michael Kölling.

from location import Location
from picks import GuitarPick, SouvenirPick, GuitarPickCollection


class CommandWords:
    def __init__(self):
        self.valid_command = ['list', 'search', 'add', 'help', 'quit']

    def is_command(self, a_string):
        if not (a_string is None):
            for command in self.valid_command:
                if command == a_string:
                    return True
        return False

    def get_all(self):
        ret_str = ''
        for command in self.valid_command:
            ret_str += command + ' '
        return ret_str


class Parser:
    def __init__(self):
        self.command_words = CommandWords()

    def get_command(self):
        '''Read the next command from the user.
        The returned command will be valid.

        returns: a valid command
        '''
        command = ''
        do = True
        while do:
            word = input('> ').strip().lower()
            if (self.command_words.is_command(word)):
                command = word
            else:
                print('Unrecognized command: ' + word)
                print('Valid commands are: ' + self.command_words.get_all())
            do = (command == '')
        return command


if __name__ == '__main__':
   parser = Parser()
   parser.get_command()
