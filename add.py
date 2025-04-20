# Simple function to test
def add(x, y):
    return x + y

# Unit Test Class for testing the add function
import unittest

class SimpleTest(unittest.TestCase):
    
    def test_addition(self):
        # Test if the addition function works correctly
        self.assertEqual(add(4, 5), 9)  # Check if 4 + 5 equals 9

    def test_add_negative(self):
        # Test with negative numbers
        self.assertEqual(add(-4, 5), 1)  # Check if -4 + 5 equals 1

    def test_add_zero(self):
        # Test with zero
        self.assertEqual(add(0, 0), 0)  # Check if 0 + 0 equals 0

# This will automatically run the tests when this script is executed
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)






