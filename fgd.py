import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_result.config(text="Температура в градусах Фаренгейта: {:.1f}".format(fahrenheit))

window = tk.Tk()
window.title("Конвертер температуры")

label_celsius = tk.Label(window, text="Введите температуру в градусах Цельсия:")
label_celsius.pack()

entry_celsius = tk.Entry(window)
entry_celsius.pack()

button_convert = tk.Button(window, text="Конвертировать", command=celsius_to_fahrenheit)
button_convert.pack()

label_result = tk.Label(window, text="")
label_result.pack() 
label = tk.Label(
    text="Привет, друг!",
    fg="white",
    bg="black",
    width=20,
    height=20
)
 
label.pack()

window.mainloop()
