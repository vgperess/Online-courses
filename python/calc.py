import tkinter as tk
from tkinter import ttk
import math

root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("400x400")
root.resizable(False, False)

entry = ttk.Entry(root, width=30, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        expression = expression.replace("sin(", "math.sin(math.radians(")
        expression = expression.replace("cos(", "math.cos(math.radians(")
        expression = expression.replace("tan(", "math.tan(math.radians(")
        expression = expression.replace("log(", "math.log10(")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

def button_scientific(operation):
    try:
        current = float(entry.get())
        entry.delete(0, tk.END)
        if operation == 'sin':
            entry.insert(0, math.sin(math.radians(current)))
        elif operation == 'cos':
            entry.insert(0, math.cos(math.radians(current)))
        elif operation == 'tan':
            entry.insert(0, math.tan(math.radians(current)))
        elif operation == 'log':
            if current > 0:
                entry.insert(0, math.log10(current))
            else:
                entry.insert(0, "Erro")
        elif operation == 'sqrt':
            if current >= 0:
                entry.insert(0, math.sqrt(current))
            else:
                entry.insert(0, "Erro")
        elif operation == 'pow':
             entry.insert(0, current**2)
    except ValueError:
        entry.insert(0, "Erro")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
    ('log', 6, 0), ('sqrt', 6, 1), ('pow', 6, 2), ('(', 5, 4), (')', 6, 4)
]

for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    elif text == 'C':
        button = ttk.Button(root, text=text, command=button_clear)
    elif text == '=':
        button = ttk.Button(root, text=text, command=button_equal)
    elif text in ['+', '-', '*', '/']:
        button = ttk.Button(root, text=text, command=lambda op=text: button_click(op))
    elif text in ['sin', 'cos', 'tan', 'log', 'sqrt', 'pow']:
        button = ttk.Button(root, text=text, command=lambda func=text: button_scientific(func))
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
