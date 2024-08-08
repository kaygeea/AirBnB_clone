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
from models.base_model import BaseModel
from models import storage
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
        print("Quitting...")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("EOF received. Exiting...")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg: str):
        """
        Create a new instance of a specified class, save it to storage, 
        and print its `id`.
        
        Usage: 
            `create BaseModel`
        
        This command supports creating instances of the `BaseModel` class.
        
        - If the class name is missing, prints: ** class name missing **
        - If the class name doesn't exist, prints: ** class doesn't exist **
        - If the class name is recognized, the new instance is created, 
        saved to the storage system, and its `id` is printed.
        
        Args:
            arg (str): The name of the class to instantiate.
        
        """
        args = arg.split()
        num_args = len(args)
        if not arg:
            print("** class name missing **")
            return
        if num_args > 1:
            print("** this method takes only 1 positional argument **")
            return
        elif arg and num_args == 1 and args[0] == BaseModel.__name__:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            return
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
