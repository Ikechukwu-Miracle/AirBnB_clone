#!/usr/bin/python3
"""This module contains the HBNBCommand class"""
import cmd
import sys
import re
import json
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A CLI for the Hbnb program.

    Attributes:
        prompt (str): prompt to display before command
        classes (list): list of classes
    """

    prompt = "(hbnb) "
    classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            ]

    def do_quit(self, line):
        """Exits the program when the user types "quit"
        and press enter
        """
        return True

    def do_EOF(self, line):
        """Exits the prompt when user clicks (crtl + d) on
        the keyboard
        """
        if sys.stdin.isatty():
            print()
        print()
        return True

    def emptyline(self):
        """Does not execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new class instance and prints its id.
        Usage: create <class>
        """

        if not check_class(arg.split()):
            return
        new_instance = eval(arg)()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id.
        Usage: show <class> <id>
        """

        args = arg.split()
        objs = storage.all()

        if not check_class(args, cls_id=True):
            return
        if "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file).
        Usage: destroy <class> <id>
        """

        args = arg.split()
        objs = storage.all()

        if not check_class(args, cls_id=True):
            return
        if "{}.{}".format(args[0], args[1]) not in objs:
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            del(objs[key])
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name.
        If no class is specified, displays all instantiated objects.
        Usage: all <class> or all
        """

        objs = storage.all()

        if not arg:
            print(["{}".format(str(v)) for _, v in objs.items()])
        else:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print(["{}".format(str(v)) for _, v in
                       objs.items() if type(v).__name__ == arg])
                return

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class> <id> <attribute> <value>
        """

        objs = storage.all()
        if "{" in arg:
            args = arg.split(" ", maxsplit=2)
            if not check_class(args, cls_id=True):
                return

            key = "{}.{}".format(args[0], args[1])
            payload: dict = json.loads(args[2])
            for key_name, val in payload.items():
                if key_name in ["id", "created_at", "updated_at"]:
                    return
                setattr(objs[key], key_name, val)
            storage.save()
            return

        args = arg.split()
        if not check_class(args, cls_id=True):
            return

        key = "{}.{}".format(args[0], args[1])
        if len(args) > 1 and key not in objs:
            print("** no instance found **")
        else:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            if args[2] in ['id', 'created_at', 'updated_at']:
                return

            attr = args[2]
            if '"' in args[3]:
                args[3] = args[3].replace('"', "")
            value = args[3]
            setattr(objs[key], attr, value)
            storage.save()

    def precmd(self, arg):
        """Defines instructions to execute before interpretation of line"""

        if not arg:
            return "\n"

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")

        arg_match = pattern.findall(arg)

        if not arg_match:
            return super().precmd(arg)

        args_tup = arg_match[0]
        if not args_tup[2]:
            if args_tup[1] == "count":
                count(args_tup)
                return "\n"
            r_var = "{} {}".format(args_tup[1], args_tup[0])
            return super().precmd(r_var)
        else:
            args = args_tup[2].split(", ")
            if len(args) == 1:
                args[0] = re.sub("[\"\']", "", args[0])
                return "{} {} {}".format(args_tup[1], args_tup[0], args[0])

            if len(args) == 3 and "{" in args[1]:
                json_args = re.findall(r"{.*}", args_tup[2])
                if json_args:
                    args[0] = re.sub("[\"\']", "", args[0])
                    json_args[0] = re.sub("\'", "\"", json_args[0])
                    return "{} {} {} {}".format(args_tup[1], args_tup[0],
                       args[0], json_args[0])

            args[0] = re.sub("[\"\']", "", args[0])
            args[1] = re.sub("[\"\']", "", args[1])
            return "{} {} {} {} {}".format(args_tup[1], args_tup[0],
              args[0], args[1], args[2])

def check_class(args, cls_id=False):
    """Validates the arguments passed to the commands"""

    if not args:
        print("** class name missing **")
        return False
    if args[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return False
    if len(args) == 1 and cls_id:
        print("** instance id missing **")
        return False
    return True

def count(arg):
    """counts the number of instances in the given class"""
    result = 0
    objs = storage.all()
    for key, val in objs.items():
        if type(val).__name__ == arg[0]:
            result += 1
    print(result)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
