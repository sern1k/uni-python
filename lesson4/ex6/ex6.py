def sum_seq(sequence):
  total = 0

  for item in sequence:
    if isinstance(item, (list, tuple)):
      total += sum_seq(item)  # Wywołujemy rekurencyjnie sum_seq na zagnieżdżonej sekwencji
    else:
      total += item  # Dodajemy liczbę do sumy

  return total


seq = [1, 2, [3, 4, (5, 6)], 7, [8, 9]]
print(sum_seq(seq))
