import unittest

from ex13 import word_length

class TestAmountOfWords(unittest.TestCase):
    def test_word_length_for_line(self):
        string = "line"
        self.assertEqual(word_length(string), 4)

    def test_word_length_for_empty_string(self):
        string = ""
        self.assertEqual(word_length(string), 0)

    def test_word_length_for_another_string(self):
        string = "Hello, World!"
        self.assertEqual(word_length(string), 13)

if __name__ == '__main__':
    unittest.main()
