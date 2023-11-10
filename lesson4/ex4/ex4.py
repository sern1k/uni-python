def fibonacci(n):
  if n < 0:
    return None
  elif n <= 1:
    return n

  fib_0, fib_1 = 0, 1

  for _ in range(2, n + 1):
    fib_n = fib_0 + fib_1
    fib_0, fib_1 = fib_1, fib_n

  return fib_1

print(fibonacci(12))
