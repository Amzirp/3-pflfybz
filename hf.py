import tkinter as tk
import random

def dice_roll():
    dice = [ "1", "2", "3", "4", "5", "6"]
    
    roll = random.randint(1, 6)
    dice_label.config(text=dice[roll - 1])

window = tk.Tk()
window.title("кинь куб")

dice_label = tk.Label(window, justify='center', font=('Courier', 14, 'bold'), height=7)
dice_label.pack(pady=10)

roll_button = tk.Button(window, text="кинь куб", command=dice_roll, font=('Arial', 12, 'bold'))
roll_button.pack(pady=10)
label = tk.Label(
    text="Привет, Tkinter!",
    foreground="yellow",  
    background="purple"  
)

window.mainloop()

