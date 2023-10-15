import unittest

from ex12 import string_from_first_chars, string_from_last_chars

class TestStringManipulation(unittest.TestCase):
    def test_first_chars_empty_line(self):
        result = string_from_first_chars("")
        self.assertEqual(result, "", "Empty line should result in an empty string.")

    def test_first_chars_single_word(self):
        result = string_from_first_chars("Word")
        self.assertEqual(result, "W", "Single word should result in the first character.")

    def test_first_chars_multiple_words(self):
        result = string_from_first_chars("This is a test")
        self.assertEqual(result, "Tiat", "Should build a string from the first characters of words.")

    def test_last_chars_empty_line(self):
        result = string_from_last_chars("")
        self.assertEqual(result, "", "Empty line should result in an empty string.")

    def test_last_chars_single_word(self):
        result = string_from_last_chars("Word")
        self.assertEqual(result, "d", "Single word should result in the last character.")

    def test_last_chars_multiple_words(self):
        result = string_from_last_chars("This is a test")
        self.assertEqual(result, "ssat", "Should build a string from the last characters of words.")

if __name__ == '__main__':
    unittest.main()
