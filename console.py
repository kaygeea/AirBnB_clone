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

    def do_show(self, arg: str):
        """
        Print the string representation of an instance based on the class name
        and `id`.

        Usage: show <class name> <id>

        - If the class name is missing, prints ** class name missing **
        - If the class name doesn't exist, prints ** class doesn't exist **
        - If the id is missing, prints ** instance id missing **
        - If no instance is found with the given id, prints ** no instance found **
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        num_args = len(args)

        if args[0] == BaseModel.__name__:
            if num_args == 2:
                all_objs = storage.all()
                this_key = ".".join(args)
                if this_key in all_objs.keys():
                    instance = BaseModel(**all_objs[this_key])
                    print(str(instance))
                    return
                else:
                    print("** no instance found **")
                    return
            elif num_args < 2:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, arg: str):
        """
        Deletes an instance based on the class name and `id`.

        Usage: destroy <class name> <id>

        - If the class name is missing, prints ** class name missing **.
        - If the class name doesn't exist, prints ** class doesn't exist **.
        - If the `id` is missing, prints ** instance id missing **.
        - If the instance of the class name doesn't exist for the id, prints ** no instance found **.

        Args:
            arg (str): The command arguments containing the class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        num_args = len(args)

        if args[0] == BaseModel.__name__:
            if num_args == 2:
                all_objs = storage.all()
                this_key = ".".join(args)
                try:
                    del all_objs[this_key]
                    storage.save()
                    return
                except KeyError:
                    print("** no instance found **")
                    return      
            elif num_args < 2:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

    def do_all(self, arg: str):
        """
        Displays the string representations of all instances in storage.

        Usage: all [<class name>]

        - If the class name is provided and doesn't exist, prints ** class doesn't exist **.
        - If no class name is provided, displays all instances.
        - The string representations of the instances are printed as a list.

        Args:
            arg (str): The optional class name to filter instances by.
        """
        args = arg.split()
        str_reps = []
        all_objs = storage.all()

        if arg and args[0] != BaseModel.__name__:
            print("** class doesn't exist **")
            return
        
        for key in all_objs.keys():
            instance = BaseModel(**all_objs[key])
            str_reps.append(str(instance))

        print(str_reps)

    def do_update(self, arg: str):
        """
        Updates an instance based on the class name and `id` by adding or
        updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        - If the class name is missing, prints ** class name missing **.
        - If the class name doesn't exist, prints ** class doesn't exist **.
        - If the `id` is missing, prints ** instance id missing **.
        - If the attribute name is missing, prints ** attribute name missing **.
        - If the value for the attribute name is missing, prints ** value missing **.
        - If the instance of the class name doesn’t exist for the id, prints ** no instance found **.

        Args:
            arg (str): The command arguments containing the class name, id,
            attribute name, and attribute value.
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        num_args = len(args)

        if args[0] == BaseModel.__name__:
            if num_args >= 4:
                all_objs = storage.all()
                this_key = f"{args[0]}.{args[1]}"
                if this_key in all_objs.keys():
                    all_objs[this_key][args[2]] = args[3]
                    instance = BaseModel(**all_objs[this_key])
                    instance.save()
                    return
                else:
                    print("** no instance found **")
                    return
            elif num_args == 3:
                print("** value missing **")
                return
            elif num_args == 2:
                print("** attribute name missing **")
                return
            elif num_args < 2:
                print("** instance id missing **")
                return
        else:
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
