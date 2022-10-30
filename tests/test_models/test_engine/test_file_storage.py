#!usr/bin/python3

''' Module tests/test_models/test_engine/test_file_storage'''

import unittest
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
import models

class TestAirbnb_Storage(unittest.TestCase):
    '''Test to class FileStorage'''

    def test_doc(self):
        """Test Docstring"""

        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_fs_class(self):
        '''Test the class of FileStorage'''
        fs = FileStorage()
        self.assertEqual(fs.__class__, FileStorage)
