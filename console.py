#!/usr/bin/python3
'''contains the entry point of the command interpreter'''


import re
import cmd
import sys
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models.city import City


class HBNBCommand(cmd.Cmd):
    '''command interpreter'''

    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''to exit the program'''
        return True

    def do_EOF(self, arg):
        '''exit the program'''
        return True

    def help_quit(self):
        '''updated and documented help'''
        print('Quit command to exit the program')

    def help_EOF(self):
        '''updated and documented help'''
        print('EOF commando to exit')

    def emptyline(self):
        '''empty line + ENTER shouldn't execute anything'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
