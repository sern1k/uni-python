def draw_rectangle(rows, cols):
    if rows < 1 or cols < 1:
        print("Prostokąt musi mieć co najmniej 1 wiersz i 1 kolumnę.")
        return

    # Inicjalizacja pustego napisu do rysowania prostokąta
    rectangle_str = ""

    for _ in range(rows):
        # Górna krawędź kratek
        rectangle_str += "+"
        rectangle_str += "---+" * cols + "\n"

        # Wnętrze kratek
        rectangle_str += "|"
        rectangle_str += "   |" * cols + "\n"

    # Dolna krawędź kratek
    rectangle_str += "+"
    rectangle_str += "---+" * cols

    # Wyświetlenie prostokąta
    print(rectangle_str)

try:
    row = int(input("Podaj długość: "))
    col = int(input("Podaj szerokość: "))
    draw_rectangle(row, col)
except ValueError:
    print("Błąd: Wprowadź liczbę całkowitą.")
