import unittest

# Import the function you want to test
from ex10 import count_words_in_string

# Define a test class that inherits from unittest.TestCase
class TestCountWordsInString(unittest.TestCase):
    # Test case for an empty string
    def test_empty_string(self):
        string = ""
        result = count_words_in_string(string)
        self.assertEqual(result, 0, "Empty string should have 0 words.")

    # Test case for a single-line string
    def test_single_line_string(self):
        string = "This is a test string."
        result = count_words_in_string(string)
        self.assertEqual(result, 5, "Should count 5 words in a single-line string.")

    # Test case for a multi-line string
    def test_multi_line_string(self):
        string = """
        This is a multi-line
        test string. Count the words.
        """
        result = count_words_in_string(string)
        self.assertEqual(result, 9, "Should count 9 words in a multi-line string.")

    # Test case for a string with multiple spaces between words
    def test_string_with_multiple_spaces(self):
        string = "This    string   has    multiple   spaces."
        result = count_words_in_string(string)
        self.assertEqual(result, 5, "Should count 5 words with multiple spaces.")

if __name__ == '__main__':
    unittest.main()
