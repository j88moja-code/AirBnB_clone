#!/usr/bin/python3

"""Defines unittest for models/base_model.py """

import unittest
import modules
from datetime import datetime
from models.base_models import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    def test_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_str(self):
        model = BaseModel()
        model_str = (
                f'[{BaseModel.__name__}], ({model.id}), <{model.__dict__}>'
            )
        self.assertequal(model_str, str(model))
