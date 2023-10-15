import unittest

from ex16 import replace_gvr_with_name

class TestReplaceGVR(unittest.TestCase):
    def test_replacement(self):
        line = "GvR"
        result = replace_gvr_with_name(line)
        self.assertEqual(result, "Guido van Rossum")

    def test_multiple_replacement(self):
        line = "GvR, GvR GvR."
        result = replace_gvr_with_name(line)
        self.assertEqual(result, "Guido van Rossum, Guido van Rossum Guido van Rossum.")

    def test_no_replacement(self):
        line = "This is an example string"
        result = replace_gvr_with_name(line)
        self.assertEqual(result, "This is an example string")

    def test_empty_string(self):
        line = ""
        result = replace_gvr_with_name(line)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
