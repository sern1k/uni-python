def flatten(sequence):
  flat_list = []

  for item in sequence:
    if isinstance(item, (list, tuple)):
      flat_list.extend(flatten(item))  # Wywołujemy rekurencyjnie flatten na zagnieżdżonej sekwencji
    else:
      flat_list.append(item)  # Dodajemy element do spłaszczonej listy

  return flat_list

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
result = flatten(seq)
print(result)
