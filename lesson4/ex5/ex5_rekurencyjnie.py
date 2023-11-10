def reverse_rec(L, left, right):
  if L is None or left < 0 or right >= len(L) or left >= right:
    return L  # Zwracamy listę bez zmiany w przypadku niepoprawnych argumentów

  if left < right:
    L[left], L[right] = L[right], L[left]
    reverse_rec(L, left + 1, right - 1)

  return L

list = [1, 2, 3, 4, 5]
print(reverse_rec(list, 1, 3))
