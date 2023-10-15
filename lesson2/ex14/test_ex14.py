import unittest

from ex14 import find_longest_word

class TestFindLongestWord(unittest.TestCase):
    def test_longest_word(self):
        line = "This is an example string"
        result = find_longest_word(line)
        self.assertEqual(result, "example")

    def test_empty_string(self):
        line = ""
        result = find_longest_word(line)
        self.assertIsNone(result)

    def test_single_word(self):
        line = "Hello"
        result = find_longest_word(line)
        self.assertEqual(result, "Hello")

    def test_multiple_longest_words(self):
        line = "The quick brown fox jumps over the lazy dog"
        result = find_longest_word(line)
        self.assertEqual(result, "quick")

if __name__ == '__main__':
    unittest.main()
