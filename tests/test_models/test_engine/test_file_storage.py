#!/usr/bin/env python3
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import mock_open, patch
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up the file.json if it exists
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_new(self):
        # Test the 'new' method
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue("BaseModel.{}".format(obj.id) in self.storage.all())

    def test_save_and_reload(self):
        # Test the 'save' and 'reload' methods
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        self.assertTrue("BaseModel.{}".format(obj1.id) in self.storage.all())
        self.assertTrue("BaseModel.{}".format(obj2.id) in self.storage.all())

if __name__ == '__main__':
    unittest.main()
