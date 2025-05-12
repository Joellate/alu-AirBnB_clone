#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes and deserializes instances to/from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for obj_dict in data.values():
                    cls_name = obj_dict["__class__"]
                    if cls_name == "BaseModel":
                        obj = BaseModel(**obj_dict)
                        self.new(obj)
        except FileNotFoundError:
            pass

