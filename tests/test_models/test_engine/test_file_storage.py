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

    def test_fs_storage(self):
        '''Test the class of storage'''
        self.assertTrue(isinstance(models.storage, FileStorage))

    def test_fs_all(self):
        ''''Test class methods exists'''
        fs = FileStorage()

        self.assertTrue(hasattr(fs, 'all'), True)
        self.assertTrue(hasattr(fs, 'new'), True)
        self.assertTrue(hasattr(fs, 'save'), True)
        self.assertTrue(hasattr(fs, 'reload'), True)

    def test_exe_all(self):
        '''Test .all generates a dict'''
        self.assertEqual(type(models.storage.all()), dict)

    def test_new_instance(self):
        '''Test creation of different instances'''
        b = BaseModel()

        models.storage.new(b)

        self.assertIn(f'{b.__class__.__name__}.{b.id}',
            models.storage.all().keys())

    def test_save_instance(self):
        '''Test saving instances in a json file'''
        b = BaseModel()

        models.storage.new(b)

        models.storage.save()

        with open('file.json') as file:
            data = file.read()

        self.assertIn(f'{b.__class__.__name__}.{b.id}', data)


if __name__ == '__main__':
    unittest.main()
