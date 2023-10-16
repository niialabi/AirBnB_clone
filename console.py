#!/usr/bin/python3
"""
Program containing entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity,
        "City": City,
        "State": State,
    }

    __objects = {
        'User': {},
        'Place': {},
        'State': {},
        'City': {},
        'Amenity': {},
        'Review': {},
    }

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves
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
        """
        Prints the str rep of an inst based on the class name and id
        """
        args = line.partition(" ")
        cmd_name = args[0]
        cmd_id = args[2]

        if not cmd_name:
            print("** class name missing **")
            return

        if cmd_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not cmd_id:
            print("** instance id missing **")
            return

        key = cmd_name + "." + cmd_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
