#!/usr/bin/python3
"""
Program containing entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id
        """
        new_base_model = eval(BaseModel())


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

    def emptyline(self):
        """
        an empty line plus ENTER shouldt execute anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id.
        """
        if not line:
            print("** class name missing **")
            return
        
        try:
            cls = globals()[line]
            instance = cls()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if (len(args) == 1):
            print("** class name missing **")
        if (len(args) > 1):
            cls_name = args[1]
            print(cls_name)
            try:
                globals()[cls_name]
            except KeyError:
                print("** class doesn't exist **")    




if __name__ == "__main__":
    HBNBCommand().cmdloop()
