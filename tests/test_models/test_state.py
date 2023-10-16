import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_instance(self):
        self.assertIsInstance(self.state, State)

    def test_state_name_default_value(self):
        self.assertEqual(self.state.name, "")

    def test_state_name_assignment(self):
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")

    def test_from_dict(self):
        state_dict = {'__class__': 'State', 'name': 'Texas'}
        new_state = State(**state_dict)
        self.assertEqual(new_state.name, 'Texas')

if __name__ == '__main__':
    unittest.main()

