import unittest

from ex8 import find_common_elements

class TestFindCommonElements(unittest.TestCase):
    def test_empty_sequences(self):
        seq1 = []
        seq2 = []
        common_elements, all_elements = find_common_elements(seq1, seq2)
        self.assertEqual(common_elements, [])
        self.assertEqual(all_elements, [])

    def test_no_common_elements(self):
        seq1 = [1, 2, 3]
        seq2 = [4, 5, 6]
        common_elements, all_elements = find_common_elements(seq1, seq2)
        self.assertEqual(common_elements, [])
        self.assertEqual(all_elements, [1, 2, 3, 4, 5, 6])

    def test_some_common_elements(self):
        seq1 = [1, 2, 3, 4, 5]
        seq2 = [4, 5, 6, 7, 8]
        common_elements, all_elements = find_common_elements(seq1, seq2)
        self.assertEqual(common_elements, [4, 5])
        self.assertEqual(all_elements, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_duplicate_elements(self):
        seq1 = [1, 2, 3, 3, 4, 4, 5]
        seq2 = [4, 4, 5, 5, 6, 6]
        common_elements, all_elements = find_common_elements(seq1, seq2)
        self.assertEqual(common_elements, [4, 5])
        self.assertEqual(all_elements, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
