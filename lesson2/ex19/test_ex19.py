import unittest

from ex19 import build_padded_blocks

class TestBuildPaddedBlocks(unittest.TestCase):
    def test_padded_blocks(self):
        L = [7, 24, 123, 6, 9]
        result = build_padded_blocks(L)
        self.assertEqual(result, ['007', '024', '123', '006', '009'])

    def test_single_digit_numbers(self):
        L = [1, 2, 3, 4, 5]
        result = build_padded_blocks(L)
        self.assertEqual(result, ['001', '002', '003', '004', '005'])

    def test_empty_list(self):
        L = []
        result = build_padded_blocks(L)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
