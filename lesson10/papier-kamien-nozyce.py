import tkinter as tk
from random import choice

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Remis"
  elif (
    (user_choice == "Kamień" and computer_choice == "Nożyce") or
    (user_choice == "Nożyce" and computer_choice == "Papier") or
    (user_choice == "Papier" and computer_choice == "Kamień")
  ):
    return "Gratulacje, wygrałeś!"
  else:
    return "Przegrałeś. Spróbuj ponownie."

def play_game(user_choice):
  computer_choice = choice(["Papier", "Kamień", "Nożyce"])
  result = determine_winner(user_choice, computer_choice)

  result_label.config(text=f"Wybór komputera: {computer_choice}\n{result}")

# GUI setup
root = tk.Tk()
root.title("Papier-Kamień-Nożyce")

# Buttons
button_paper = tk.Button(root, text="Papier", command=lambda: play_game("Papier"))
button_paper.pack(side=tk.LEFT, padx=10)

button_rock = tk.Button(root, text="Kamień", command=lambda: play_game("Kamień"))
button_rock.pack(side=tk.LEFT, padx=10)

button_scissors = tk.Button(root, text="Nożyce", command=lambda: play_game("Nożyce"))
button_scissors.pack(side=tk.LEFT, padx=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
