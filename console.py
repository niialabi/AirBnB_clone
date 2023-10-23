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
import shlex


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

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
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
        if not storage._FileStorage__objects[key]:
            print("** no instance found **")
        else:
            obj_instances = storage.all()
            del obj_instances[key]
            storage.save()

    def do_all(self, line=None):
        """
        Prints all string representation of all 
        instances based or not on the class name.
        Args:
            line(optional string)
        """
        all_instances = storage.all()
        input_arr = shlex.split(line)
        if len(input_arr) == 1 and input_arr[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print_res = []
        for inst in all_instances:
            if len(input_arr) == 0 or (
                len(input_arr) > 0
                and input_arr[0] == all_instances[inst].to_dict()["__class__"]
            ):
                print_res.append(str(all_instances[inst]))
        print(print_res)

    def do_update(self, line, arg=0):
        """
        update <class name> <id> <attribute name> "<attribute value>"
        """
        all_instances = storage.all()
        if not arg:
            input_arr = shlex.split(line)
        else:
            input_arr = line

        if len(input_arr) < 4:
            print("** Invalid command format **")
            return

        cmd_name = input_arr[0]
        cmd_id = input_arr[2]

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

        if key not in all_instances:
            print("** no instance found **")
            return

        attr_name = input_arr[3]
        attr_value = input_arr[4]

        instance = all_instances[key]

        # Check if the attribute exists on the instance
        if hasattr(instance, attr_name):
            attr_value = type(getattr(instance, attr_name))(attr_value)
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")





if __name__ == "__main__":
    HBNBCommand().cmdloop()
