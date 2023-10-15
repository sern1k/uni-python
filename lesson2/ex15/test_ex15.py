import unittest

from ex15 import concatenate_numbers

class TestConcatenateNumbers(unittest.TestCase):
    def test_concatenation(self):
        L = [12, 34, 56, 78]
        result = concatenate_numbers(L)
        self.assertEqual(result, "12345678")

    def test_empty_list(self):
        L = []
        result = concatenate_numbers(L)
        self.assertEqual(result, "")

    def test_single_number(self):
        L = [1]
        result = concatenate_numbers(L)
        self.assertEqual(result, "1")

if __name__ == '__main__':
    unittest.main()
