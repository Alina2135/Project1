import tkinter as tk
from tkinter import messagebox

# Функція обробки натискань кнопок
def click(button_text):
    try:
        if button_text == "=":
           # ========== ЗМІНЕНО ДЛЯ БАГУ #4 ==========
            # Проблема: програма вилітає при діленні на нуль
            # Виправлення: перевіряємо, чи є ділення на нуль, і показуємо помилку
            expression = entry.get()                    # ЗМІНЕНО: отримуємо вираз
            if "/0" in expression:                      # ЗМІНЕНО: перевіряємо ділення на нуль
                messagebox.showerror("Помилка", "Ділення на нуль неможливе!")
                return                                   # ЗМІНЕНО: виходимо з функції
            result = str(eval(expression))              # ЗМІНЕНО: обчислюємо вираз
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
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

# ========== ЗМІНЕНО ДЛЯ БАГУ #3 ==========
# Проблема: кнопка "=" знаходиться в нелогічному місці (не в кінці)
# Виправлення: змінюємо порядок кнопок – "=" тепер в самому кінці
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', 'C', '0', '+',   # ЗМІНЕНО: "=" прибрано звідси, додано "C" та "0"
    '='                    # ЗМІНЕНО: "=" тепер окремо в кінці списку
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
