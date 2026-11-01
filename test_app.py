import unittest
from app import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Ana"), "Hello, Ana!")

    def test_strip(self):
        self.assertEqual(greet(" Leo "), "Hello, Leo!")

    def test_empty(self):
        with self.assertRaises(ValueError):
            greet(" ")

if __name__ == "__main__":
    unittest.main()