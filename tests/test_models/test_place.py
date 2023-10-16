import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_place_instance(self):
        self.assertIsInstance(self.place, Place)

    def test_place_attributes_default_values(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_attributes_assignment(self):
        self.place.city_id = "12345"
        self.place.user_id = "user123"
        self.place.name = "Cozy Cabin"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 150
        self.place.latitude = 34.12345
        self.place.longitude = -118.67890
        self.place.amenity_ids = [1, 2, 3]
        
        self.assertEqual(self.place.city_id, "12345")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 34.12345)
        self.assertEqual(self.place.longitude, -118.67890)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    def test_from_dict(self):
        place_dict = {
            '__class__': 'Place',
            'city_id': '54321',
            'user_id': 'user456',
            'name': 'Sunny Villa',
            'number_rooms': 4,
            'number_bathrooms': 3,
            'max_guest': 8,
            'price_by_night': 250,
            'latitude': 35.6789,
            'longitude': -120.9876,
            'amenity_ids': [4, 5, 6]
        }
        new_place = Place(**place_dict)
        self.assertEqual(new_place.city_id, '54321')
        self.assertEqual(new_place.user_id, 'user456')
        self.assertEqual(new_place.name, 'Sunny Villa')
        self.assertEqual(new_place.number_rooms, 4)
        self.assertEqual(new_place.number_bathrooms, 3)
        self.assertEqual(new_place.max_guest, 8)
        self.assertEqual(new_place.price_by_night, 250)
        self.assertEqual(new_place.latitude, 35.6789)
        self.assertEqual(new_place.longitude, -120.9876)
        self.assertEqual(new_place.amenity_ids, [4, 5, 6])

if __name__ == '__main__':
    unittest.main()

