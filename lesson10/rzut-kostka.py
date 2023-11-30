import tkinter as tk
from random import randint
from PIL import Image, ImageTk

def roll_dice():
    result = randint(1, 6)
    update_result_label(result)

def update_result_label(result):
    result_label.config(text=f"Wynik rzutu: {result}")
    update_dice_image(result)

def update_dice_image(result):
    image_path = f"dice_images/dice_{result}.png"
    image = Image.open(image_path)
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

# GUI setup
root = tk.Tk()
root.title("Symulator rzutu kostką")

# Button
roll_button = tk.Button(root, text="Rzuć kostką", command=roll_dice)
roll_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Dice Image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Run the GUI
root.mainloop()
