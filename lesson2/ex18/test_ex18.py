import unittest

from ex18 import count_zeros_in_large_number

class TestCountZerosInLargeNumber(unittest.TestCase):
    def test_count_zeros(self):
        number = 10203040506070
        result = count_zeros_in_large_number(number)
        self.assertEqual(result, 7)

    def test_no_zeros(self):
        number = 123456789
        result = count_zeros_in_large_number(number)
        self.assertEqual(result, 0)

    def test_only_zero(self):
        number = 0
        result = count_zeros_in_large_number(number)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
