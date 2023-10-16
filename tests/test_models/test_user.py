import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User()

    def test_default_attributes(self):
        # Check if the default attributes are empty strings
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_set_attributes(self):
        # Set values for the attributes and check if they are set correctly
        self.user.email = "user@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()

