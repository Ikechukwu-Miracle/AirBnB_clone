#!/usr/bin/python3
"""This module contains the HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program when the user types "quit"
        and press enter
        """
        return True

    def do_EOF(self, line):
        """Exits the prompt when user clicks (crtl + d) on
        the keyboard
        """
        print()
        return True

    def emptyline(self):
        """Does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
