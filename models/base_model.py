#!/usr/bin/python3
''' module for BaseModel class '''

import uuid
import datetime
import engine.file_storage as storage


class BaseModel:
       """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        ''' saves a model '''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary representation of the model '''
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

    def __str__(self):
        ''' returns a string representation of the model '''
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)
