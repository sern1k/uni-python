while True:
    user_input = input("Wprowadź liczbę rzeczywistą (lub 'stop' aby zakończyć): ")

    if user_input.lower() == "stop":
        break

    try:
        x = float(user_input)
        x_cubed = x ** 3
        print(f"x: {x}, x^3: {x_cubed}")
    except ValueError:
        print("Błąd: To nie jest liczba rzeczywista. Spróbuj ponownie.")
