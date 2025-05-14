#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models import classes


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        return True

    def emptyline(self):
        """nothing done when an empty line is entered"""
        pass

    def do_create(self, arg):

        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            model = classes[arg]()
            storage.new(model)
            storage.save()
            print(model.id)

    def help_create(self):
        print("Create command to create a new object")

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            arr = arg.split(" ")
            if arr[0] not in classes.keys():
                print("** class doesn't exist **")
            elif len(arr) < 2:
                print("** instance id missing **")
            else:
                all_items = storage.all()
                item = all_items.get("{}.{}".format(arr[0], arr[1]))
                if not item:
                    print("** no instance found **")
                else:
                    print(item)

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            arr = arg.split(" ")
            if arr[0] not in classes.keys():
                print("** class doesn't exist **")
            elif len(arr) < 2:
                print("** instance id missing **")
            else:
                all_items = storage.all()
                item = all_items.get("{}.{}".format(arr[0], arr[1]))
                if not item:
                    print("** no instance found **")
                else:
                    del all_items["{}.{}".format(arr[0], arr[1])]
                    storage.save()

    def do_all(self, arg):
        if not arg:
            items = storage.all()
            arr = [str(items[i]) for i in items.keys()]
            print(arr)
        else:
            if arg not in classes.keys():
                print("** class doesn't exist **")
            else:
                items = storage.all()
                arr = [str(items[i]) for i in items.keys()
                       if items[i].__class__.__name__ == arg]
                print(arr)

    def do_update(self, arg):
        arr = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif arr[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            items = storage.all()
            item = items.get("{}.{}".format(arr[0], arr[1]))
            if not item:
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
            elif len(arr) < 4:
                print("** value missing **")
            else:
                setattr(item, arr[2], arr[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
