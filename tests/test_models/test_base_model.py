import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Create a new BaseModel instance for testing
        self.base_model = BaseModel()

    def test_init_with_kwargs(self):
        # Test instantiating  method with kwargs
        data = {
            "id": "test_id",
            "created_at": "2023-10-12T10:00:00.123456",
            "updated_at": "2023-10-12T11:00:00.123456",
            "custom_field": "custom_value"
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, "test_id")
        self.assertEqual(obj.custom_field, "custom_value")
        self.assertEqual(obj.created_at, datetime(2023, 10, 12, 10, 0, 0, 123456))
        self.assertEqual(obj.updated_at, datetime(2023, 10, 12, 11, 0, 0, 123456))

    def test_save(self):
        # Test save method
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        # Test to_dict method
        data = self.base_model.to_dict()
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data["id"], self.base_model.id)
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertEqual(data["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(data["updated_at"], self.base_model.updated_at.isoformat())

    def test_str(self):
        # Test str method
        obj_str = str(self.base_model)
        self.assertTrue(obj_str.startswith("[BaseModel]"))
        self.assertIn(self.base_model.id, obj_str)

if __name__ == '__main__':
    unittest.main()

