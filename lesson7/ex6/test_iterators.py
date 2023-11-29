import unittest
import itertools
import random

class TestIterators(unittest.TestCase):
  def test_binary_iterator(self):
    binary_iterator = itertools.cycle([0, 1])
    expected_output = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    actual_output = [next(binary_iterator) for _ in range(15)]
    self.assertEqual(actual_output, expected_output)

  # poniższe dwa testy używają modułu random, więc nie jestem w stanie przetestować konkretnego wyniku,
  # mogę sprawdzić jedynie, czy wartości są z danego przedziału/zbioru
  def test_directions_iterator(self):
    directions = ["N", "E", "S", "W"]
    directions_iterator = iter(lambda: random.choice(directions), 1)
    for _ in range(15):
      self.assertIn(next(directions_iterator), directions)

  def test_days_iterator(self):
    days_iterator = (random.choice(range(1, 8)) for _ in iter(int, 1))
    for _ in range(15):
      self.assertIn(next(days_iterator), range(1, 8))

if __name__ == '__main__':
  unittest.main()
