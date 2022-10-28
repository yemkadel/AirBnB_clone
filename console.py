#!/usr/bin/python3
""" This is the console module """
import cmd
import shlex
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This class defines the HBNBCommand class """
    prompt = '(hbnb) '
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Create command to create new BaseModel"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            if arg in self.classes:
                if arg == "BaseModel":
                    inst = BaseModel()
                    print(inst.id)
                    inst.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show Command prints the str representation of an instance"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                theKey = "{}.{}".format(args[0], args[1])
                if theKey in instances.keys():
                    print(instances[theKey])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command deletes an instance
        based on the class name and id"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = arg.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instances = storage.all()
                theKey = "{}.{}".format(args[0], args[1])
                if theKey in instances.keys():
                    storage.delete(instances[theKey])
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        instances = storage.all()
        if len(arg) < 1:
            print(["{}".format(instance) for instance in instances.values()])
        else:
            args = arg.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print(["{}".format(v) for k, v in instances.items()
                      if k.split(".")[0] == args[0]])

    def do_update(self, arg):
        """Update Command updates the instance
        based on the class name and id"""
        if len(arg) < 1:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instances = storage.all()
                theKey = "{}.{}".format(args[0], args[1])
                if theKey in instances.keys():
                    instances[theKey].__dict__[args[2]] = str(args[3])
                    storage.save()
                else:
                    print("** no instance found **")

    def emptyline(self):
        """ This method handles emptyline entry """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
