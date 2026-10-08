import unittest
from app import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Ana"), "Hello, Ana")

if __name__ == "__main__":
    unittest.main()
