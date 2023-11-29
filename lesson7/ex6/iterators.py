# a
import itertools

binary_iterator = itertools.cycle([0, 1])

print('binary iterator:')
for _ in range(15):
  print(f"{next(binary_iterator)}")

# b
import random

directions = ["N", "E", "S", "W"]

directions_iterator = iter(lambda: random.choice(directions), 1)

print('\ndirections iterator:')
for _ in range(15):
  print(f"{next(directions_iterator)}")

#c
days_iterator = (random.choice(range(1, 8)) for _ in iter(int, 1))

print('\ndays iterator:')
for _ in range(15):
  print(f"{next(days_iterator)}")
