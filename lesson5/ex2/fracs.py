from math import gcd

def add_frac(frac1, frac2):
  if frac1[0] == 0:
    return frac2
  elif frac2[0] == 0:
    return frac1

  minus(frac1)
  minus(frac2)

  result = [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]
  return simplify_frac(result)

def sub_frac(frac1, frac2):
  if frac1[0] == 0:
    return simplify_frac([-1* frac2[0], frac2[1]])
  if frac2[0] == 0:
    return frac1

  return add_frac(frac1, [-frac2[0], frac2[1]])

def mul_frac(frac1, frac2):
  result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
  return simplify_frac(result)

def div_frac(frac1, frac2):
  return mul_frac(frac1, [frac2[1], frac2[0]])

def is_positive(frac):
  return frac[0] * frac[1] > 0

def is_zero(frac):
  return frac[0] == 0

def cmp_frac(frac1, frac2):
  simplify_frac(frac1)
  simplify_frac(frac2)
  diff = sub_frac(frac1, frac2)
  if diff[0] < 0:
    return -1
  elif diff[0] > 0:
    return 1
  else:
    return 0

def frac2float(frac):
  return frac[0] / frac[1]

def simplify_frac(frac):
  if frac[1] == 0:
    return "0 w mianowniku"
  minus(frac)
  nwd = gcd(frac[0], frac[1])
  return [frac[0] // nwd, frac[1] // nwd]

def minus(frac):
  if frac[1] < 0:
    frac[1] *= -1
    frac[0] *= -1

f1 = [-1, 2]      # -1/2
f2 = [1, -2]      # -1/2 (niejednoznaczność)
f3 = [0, 1]       # zero
f4 = [0, 2]       # zero (niejednoznaczność)
f5 = [3, 1]       # 3
f6 = [6, 2]       # 3 (niejednoznaczność)

print("\naddition")
print("f1 + f2 =", add_frac(f1, f2))
print("f1 + f3 =", add_frac(f1, f3))

print("\nsubtraction")
print("f1 - f3 =", sub_frac(f1, f3))
print("f3 - f1 =", sub_frac(f3, f1))
print("f1 - f2 =", sub_frac(f1, f2))

print("\nmultiplication")
print("f5 * f6 =", mul_frac(f5, f6))
print("f4 * f6 =", mul_frac(f4, f6))
print("f2 * f5 =", mul_frac(f2, f5))

print("\ndivision")
print("f5 / f6 =", div_frac(f5, f6))
print("f1 / f6 =", div_frac(f1, f6))

print("\nis positive")
print("Is f1 positive?", is_positive(f1))
print("Is f2 positive?", is_positive(f2))
print("Is f3 positive?", is_positive(f3))
print("Is f5 positive?", is_positive(f5))

print("\nis zero")
print("Is f1 zero?", is_zero(f1))
print("Is f3 zero?", is_zero(f3))
print("Is f4 zero?", is_zero(f4))
print("Is f6 zero?", is_zero(f6))

print("\ncompare")
print("Compare f1 and f2:", cmp_frac(f1, f2))
print("Compare f3 and f4:", cmp_frac(f3, f4))
print("Compare f5 and f6:", cmp_frac(f5, f6))
print("Compare f1 and f6:", cmp_frac(f1, f6))
print("Compare f6 and f1:", cmp_frac(f6, f1))

print("\ncompare")
print("f5 as float:", frac2float(f5))
print("f3 as float:", frac2float(f3))
print("f2 as float:", frac2float(f2))
