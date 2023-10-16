import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_instance(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_name_default_value(self):
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name_assignment(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")

    def test_from_dict(self):
        amenity_dict = {'__class__': 'Amenity', 'name': 'Gym'}
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.name, 'Gym')

if __name__ == '__main__':
    unittest.main()

