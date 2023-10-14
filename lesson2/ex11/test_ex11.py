import unittest
from ex11 import add_underscore_between_characters

class TestAddUnderscoreBetweenCharacters(unittest.TestCase):
    def test_empty_string(self):
        input_string = ""
        result = add_underscore_between_characters(input_string)
        self.assertEqual(result, "", "Empty string should remain empty.")

    def test_single_character_string(self):
        input_string = "A"
        result = add_underscore_between_characters(input_string)
        self.assertEqual(result, "A", "Single character string should remain the same.")

    def test_word_without_underscores(self):
        input_string = "word"
        result = add_underscore_between_characters(input_string)
        self.assertEqual(result, "w_o_r_d", "Should add underscores between characters.")

if __name__ == '__main__':
    unittest.main()
