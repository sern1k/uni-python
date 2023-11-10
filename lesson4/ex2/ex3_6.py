def make_grid(rows, cols):
    if rows < 1 or cols < 1:
        print("Prostokąt musi mieć co najmniej 1 wiersz i 1 kolumnę.")
        return

    rectangle_str = ""

    for _ in range(rows):
        rectangle_str += "+"
        rectangle_str += "---+" * cols + "\n"

        rectangle_str += "|"
        rectangle_str += "   |" * cols + "\n"

    rectangle_str += "+"
    rectangle_str += "---+" * cols

    return rectangle_str

print(make_grid(2, 4))
