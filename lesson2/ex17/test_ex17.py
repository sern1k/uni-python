import unittest

from ex17 import sort_words_alphabetically, sort_words_by_length

class TestWordSorting(unittest.TestCase):
    def test_sort_alphabetically(self):
        line = "This is an example string to sort"
        result = sort_words_alphabetically(line)
        expected = ['an', 'example', 'is', 'sort', 'string', 'This', 'to']
        self.assertEqual(result, expected)

    def test_sort_by_length(self):
        line = "This is an example string to sort"
        result = sort_words_by_length(line)
        expected = ['is', 'an', 'to', 'This', 'sort', 'string', 'example']
        self.assertEqual(result, expected)

    def test_empty_string(self):
        line = ""
        result_alpha = sort_words_alphabetically(line)
        result_length = sort_words_by_length(line)
        self.assertEqual(result_alpha, [])
        self.assertEqual(result_length, [])

if __name__ == '__main__':
    unittest.main()
