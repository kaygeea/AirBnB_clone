#!/usr/bin/python3
"""Contains entry point of command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter to allow interactive program usage"""
    # intro = '\033[1;32mWelcome to the HBNB shell.\
    #         \nType \'help\' or \'?\' to see command options.'
    prompt = '\033[1;37;40m(hbnb) '

    def do_quit(self, line):
        """Type command to exit the program\n"""
        # print('You\'re exiting the shell...')
        # print('Bye!!!')
        return True

    def do_EOF(self, line):
        """Command to exit the program\n"""
        # print('\033[1;31;40m\nYou\'re exiting the shell...')
        # print('Bye!!!')
        # print('\033[1;37;40m')
        return True

    def emptyline(self):
        """Overwrite default emptyline behaviour of executing prev command"""
        new_emptyline = ''
        return new_emptyline


if __name__ == '__main__':
    HBNBCommand().cmdloop()
