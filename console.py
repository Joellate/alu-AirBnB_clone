#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        if line == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        parts = line.split()
        if len(parts) == 0:
            print("** class name missing **")
        elif parts[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        else:
            key = f"{parts[0]}.{parts[1]}"
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

