# This is a command line interface for the GuitarPickCollection class
# It borrows heavily from code presented in the BlueJ book
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
        """Read the next command from the user.
        The returned command will be valid.

        returns: a valid command
        """
        command = ''
        value = ''
        do = True
        while do:
            wordlist = input('> ').strip().lower().split()
            word = wordlist[0]
            if (self.command_words.is_command(word)):
                command = word
                if len(wordlist) >= 2:
                    value = wordlist[1]
            else:
                print('Unrecognized command: ' + word)
                print('Valid commands are: ' + self.command_words.get_all())
            do = (command == '')
        return command, value



class PickCollectionTextInterface:

    def __init__(self):
        self.collection = GuitarPickCollection()
        self.parser = Parser()

#helper methods to implement commands
    def _list(self, value):
        self.collection.list_all()

    def _search(self, value):
        pass

    def _add(self, value):
        self._add_souvenir()

    def _add_souvenir(self):
        name = input('Name of pick: ')
        color = input('Color of pick: ')
        city = input('From where (city): ')
        state = input('(state): ')
        year = input('When (year): ')
        play = input('Is it a real pick? ')
        if play.strip().lower()[0] == 'n':
            functional = False
        else:
            functional = True
        self.collection.add_pick(SouvenirPick(
            name,
            Location(city, state),
            year,
            color,
            functional
        ))

    def _help(self, value):
        if value == '':
            print('Valid commands are:')
            print(self.parser.command_words.get_all())
        else:
            meaning = self.parser.command_words.valid_commands[value]
            print(f"{value}: {meaning}")

    def _about(self, value):
        print('Guitar Pick Collection')

    def _quit(self, value):
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
            command, value  = self.parser.get_command()
            func = switcher.get(command)
            func(value)
            do = (not command == 'quit')

        print('Good bye')




def main():
    text_interface = PickCollectionTextInterface()
    text_interface.run()


if __name__ == '__main__':
   main()
