# This is a command line interface for the GuitarPickCollection class
# It borrows heavily from code done in the BlueJ book
# by David J. Barnes and Michael Kölling.

from location import Location
from picks import GuitarPick, SouvenirPick, GuitarPickCollection


class CommandWords:
    def __init__(self):
        self.valid_commands = {
            'list': 'list all picks',
             'search': 'search for a pick',
              'add': 'add a souvenir pick to the collection',
              'help': 'list all commands',
              'about': 'display app information',
              'quit': 'exit the program'
        }
    def is_command(self, a_string):
        if not (a_string is None):
            for command in self.valid_commands.keys():
                if command == a_string:
                    return True
        return False

    def get_all(self):
        ret_str = ''
        for command in self.valid_commands.keys():
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



class PickCollectionTextInterface:

    def __init__(self):
        self.collection = GuitarPickCollection()
        self.parser = Parser()

#helper methods to implement commands
    def _list(self, command):
        pass

    def _search(self, command):
        pass

    def _add(self, command):
        pass

    def _help(self, command):
        pass

    def _about(self, command):
        print('Guitar Pick Collection')

    def _quit(self, command):
        pass

    def run(self):
        switcher = {
            'list': self._list,
            'search': self._search,
            'add': self._add,
            'help': self._help,
            'about': self._about,
            'quit': self._quit
        }

        print('Guitar Pick Collection')
        print('Type "help" for a list of command')

        command = ''
        do = True
        while do:
            command = self.parser.get_command()
            func = switcher.get(command)
            func(command)
            do = (not command == 'quit')

        print('Good bye')




def main():
    text_interface = PickCollectionTextInterface()
    text_interface.run()


if __name__ == '__main__':
   main()
