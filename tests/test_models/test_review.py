import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_review_instance(self):
        self.assertIsInstance(self.review, Review)

    def test_review_attributes_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_attributes_assignment(self):
        self.review.place_id = "12345"
        self.review.user_id = "user123"
        self.review.text = "A wonderful stay"
        
        self.assertEqual(self.review.place_id, "12345")
        self.assertEqual(self.review.user_id, "user123")
        self.assertEqual(self.review.text, "A wonderful stay")

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")

    def test_from_dict(self):
        review_dict = {
            '__class__': 'Review',
            'place_id': '54321',
            'user_id': 'user456',
            'text': 'Great experience!'
        }
        new_review = Review(**review_dict)
        self.assertEqual(new_review.place_id, '54321')
        self.assertEqual(new_review.user_id, 'user456')
        self.assertEqual(new_review.text, 'Great experience!')

if __name__ == '__main__':
    unittest.main()

