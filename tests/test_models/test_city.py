import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_instance(self):
        self.assertIsInstance(self.city, City)

    def test_city_state_id_default_value(self):
        self.assertEqual(self.city.state_id, "")

    def test_city_name_default_value(self):
        self.assertEqual(self.city.name, "")

    def test_city_state_id_assignment(self):
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_city_name_assignment(self):
        self.city.name = "Los Angeles"
        self.assertEqual(self.city.name, "Los Angeles")

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")

    def test_from_dict(self):
        city_dict = {'__class__': 'City', 'state_id': 'NY', 'name': 'New York City'}
        new_city = City(**city_dict)
        self.assertEqual(new_city.state_id, 'NY')
        self.assertEqual(new_city.name, 'New York City')

if __name__ == '__main__':
    unittest.main()

