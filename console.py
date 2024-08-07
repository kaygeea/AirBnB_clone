#!/usr/bin/env python3
"""
Console module for the HBNB application.

This module contains the entry point of the command interpreter.
The command interpreter allows users to interact with the HBNB
application, providing commands to manage and manipulate objects.

Classes:
    HBNBCommand: Command interpreter class for the HBNB application.

Usage:
    Run this script directly to start the command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB application.
    
    This class provides a command-line interface for interacting with
    the HBNB application, allowing users to execute commands and manage
    HBNB objects.

    Methods:
        do_quit: Quit command to exit the program.
        do_EOF: EOF command to exit the program.
        emptyline: Do nothing on empty input line.
        do_help: Show help for a command.
    """
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
