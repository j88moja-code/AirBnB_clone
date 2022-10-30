#!/usr/bin/python3
import models
import uuid
from datetime import datetime


class BaseModel():
    '''class Base'''
    def __init__(self, *args, **kwargs):
        '''constructor class'''

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.now()
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''string representation'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

