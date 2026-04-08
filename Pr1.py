import tkinter as tk
from tkinter import messagebox

# Функція обробки натискань кнопок
def click(button_text):
    try:
        if button_text == "=":
            # Функціональна помилка 1: ділення на нуль не обробляється
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "C":
            # Функціональна помилка 2: кнопка очищення не очищає повністю
            entry.delete(0, tk.END)
            entry.insert(tk.END, " ")  # залишається пробіл
        elif button_text == "0":
            # Функціональна помилка 3: нуль не додається
            pass
        else:
            entry.insert(tk.END, button_text)
    except:
        # Повідомлення про помилку
        messagebox.showerror("Помилка", "Невірна операція!")

root = tk.Tk()
root.title("Пробний Калькулятор")

# UI/UX помилка 1: низький контраст кнопок (світлий текст на світлому фоні)
root.configure(bg="#2d2d2d")  # темний фон

# Коментар з main

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Кнопки калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '=', '+',
    'C', '0'
]

row = 1
col = 0
for b in buttons:
     # ========== ЗМІНЕНО: кнопки темніші ==========
    button = tk.Button(root, text=b, width=7, height=3,
                       bg="#555555", fg="white",  # ЗМІНЕНО: було bg="lightgray", fg="white"
                       font=("Arial", 12, "bold"),
                       command=lambda x=b: click(x))
    button.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# UI/UX помилка 3: кнопка "=" не в кінці ряду (зміщена)

root.mainloop()
