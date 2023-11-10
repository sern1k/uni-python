import unittest

from ex3_6 import make_grid

class TestMakeGrid(unittest.TestCase):
    def test_make_grid_positive(self):
        result = make_grid(3, 4)
        expected_result = (
            "+---+---+---+---+\n"
            "|   |   |   |   |\n"
            "+---+---+---+---+\n"
            "|   |   |   |   |\n"
            "+---+---+---+---+\n"
            "|   |   |   |   |\n"
            "+---+---+---+---+"
        )
        self.assertEqual(result, expected_result)

    def test_make_grid_negative(self):
        result = make_grid(0, 2)
        self.assertIsNone(result)

if __name__ == '__main__':
  unittest.main()
