#!/usr/bin/python3
"""
Program containing entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """
        End of file signal ends program
        """
        return True

    def do_quit(self, line):
        """
        "quit" ends program cleanly
        """
        return True

    def empty_line(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
