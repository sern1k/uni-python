def draw_ruler(length):
    if length < 1:
        print("Miarka musi mieć co najmniej długość 1.")
        return

    # Inicjalizacja pustego napisu do rysowania miarki
    ruler_str = ""
    numbers_str = ""

    for i in range(length + 1):
        numbers_str += str(i)
        if i < 9:
            numbers_str += "    "
        else:
            numbers_str += "   "
        ruler_str += "|...."

    # Usunięcie ostatnich 4 znaków (nadmiarowych kropek i spacji) z napisu miarki
    ruler_str = ruler_str[:-4]
    numbers_str = numbers_str[:-1]

    print(ruler_str)
    print(numbers_str)

try:
    length = int(input("Podaj długość miarki: "))
    draw_ruler(length)
except ValueError:
    print("Błąd: Wprowadź liczbę całkowitą jako długość miarki.")
