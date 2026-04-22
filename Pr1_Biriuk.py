import tkinter as tk
from tkinter import messagebox


# ========== ЛОГІКА  ==========

def calculate(expression):
    """Функція для обчислення математичного виразу"""
    try:
        if "/0" in expression:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Ділення на нуль!")
    except:
        raise ValueError("Невірний вираз!")


# ========== GUI (інтерфейс) ==========

def click(button_text):
    try:
        if button_text == "=":
            expression = entry.get()
            result = str(calculate(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)
    except ZeroDivisionError as e:
        messagebox.showerror("Помилка", str(e))
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))


root = tk.Tk()
root.title("Калькулятор")
root.configure(bg="#2d2d2d")

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', 'C', '0', '+',
    '='
]

row = 1
col = 0
for b in buttons:
    button = tk.Button(root, text=b, width=7, height=3,
                       bg="#555555", fg="white",
                       font=("Arial", 12, "bold"),
                       command=lambda x=b: click(x))
    button.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()