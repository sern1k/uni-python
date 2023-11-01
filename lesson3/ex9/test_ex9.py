import unittest

from ex9 import sum_of_sequences

class TestSumOfSequences(unittest.TestCase):
    def test_empty_sequences(self):
        sequences = []
        sums = sum_of_sequences(sequences)
        self.assertEqual(sums, [])

    def test_single_sequence(self):
        sequences = [[1, 2, 3]]
        sums = sum_of_sequences(sequences)
        self.assertEqual(sums, [6])

    def test_multiple_sequences(self):
        sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
        sums = sum_of_sequences(sequences)
        self.assertEqual(sums, [0, 4, 3, 7, 18])

    def test_sequences_with_negative_numbers(self):
        sequences = [(1, -2, 3), [-4, 5, -6]]
        sums = sum_of_sequences(sequences)
        self.assertEqual(sums, [2, -5])

if __name__ == "__main__":
    unittest.main()
