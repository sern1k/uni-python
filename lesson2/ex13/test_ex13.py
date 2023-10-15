import unittest

from ex13 import amount_of_words

class TestAmountOfWords(unittest.TestCase):
    def test_empty_line(self):
        result = amount_of_words("")
        self.assertEqual(result, 0, "Empty line should have 0 words.")

    def test_single_word(self):
        result = amount_of_words("Word")
        self.assertEqual(result, 1, "A single word should be counted as one word.")

    def test_multiple_words(self):
        result = amount_of_words("This is a test")
        self.assertEqual(result, 4, "A line with multiple words should count them correctly.")

if __name__ == '__main__':
    unittest.main()
