#!/usr/bin/python3
'''contains the entry point of the command interpreter'''

import cmd
import models
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
import os

class HBNBCommand(cmd.Cmd):
    '''command interpreter'''

    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''to exit the program'''
        return True
