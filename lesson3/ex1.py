x = 2; y = 3;   # nie piszemy w języku Python średnika na końcu linii, przypisanie zmiennych powinno być w różnych liniach
if (x > y):
    result = x;
else:
    result = y;
# kod się skompiluje i wykona poprawnie, jednak nie jest zgodny z ogólnymi zasadami pisania kodu w języku Python


for i in "axby": if ord(i) < 100: print (i)     # if powinien być w osobnym wierszu ze wcięciem
# kod się nie skompiluje, nie jest poprawny składniowo

for i in "axby": print (ord(i) if ord(i) < 100 else i)  # ten fragment jest poprawny składniowo


# Poprawny kod, zgodny z zasadami pisania w języku Python:
x = 2
y = 3
if x > y:
    result = x
else:
    result = y

for i in "axby":
    if ord(i) < 100:
        print(i)

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
