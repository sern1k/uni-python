# metoda .sort() zwraca None, więc L = None
# metoda .sort() sortuje w miejscu, więc dodatkowe przypisanie nie jest potrzebne
L = [3, 5, 4] ; L = L.sort()
# Poprawny kod:
L = [3, 5, 4]
L.sort()

# tutaj próbujemy przypisać 3 wartości do 2 zmiennych
x, y = 1, 2, 3
# Poprawny kod:
x, y, z = 1, 2, 3

# krotki w Pythonie są niemutowalne, czyli nie można zmieniać ich wartości
# jeśli potrzebujemy zmienić wartości lepiej jest użyć listy
X = 1, 2, 3 ; X[1] = 4
# Poprawny kod:
X = [1, 2, 3]
X[1] = 4

# indeksacja zaczyna się od 0, tutaj mamy indeksy 0, 1, 2 a próbujemy przypisać pod 3, który nie istnieje
X = [1, 2, 3] ; X[3] = 4
# Poprawny kod:
X = [1, 2, 3]
X[2] = 4 # oczywiście X[0], X[1] również mogło być, jednak zakładam, że chcieliśmy się dostać do ostatniego elementu

# X jest stringiem, a metoda append jest dla list
X = "abc" ; X.append("d")
# Poprawny kod:
X = "abc"
X += "d"
# lub inna opcja, chociaż bardziej przekombinowana, daje ten sam wynik
X = ["a", "b", "c"]
X.append("d")
X = "".join(X)

# brakuje podania na jakiej liście ma zostać wykonane
L = list(map(pow, range(8)))
# Poprawny kod:
L = list(map(pow, L, range(8)))
