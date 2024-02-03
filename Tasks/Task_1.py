import tkinter as tk

"""
Решите задачу: напишите простейший калькулятор, состоящий из двух
текстовых полей,куда пользователь вводит числа, и четырех кнопок
"+", "-", "*", "/". Результат вычисления должен отображаться
в метке. Если арифметическое действие выполнить невозможно (например,
если были введены буквы, а не числа), то в метке должно появляться слово
"ошибка".
"""


def calculate(operation):
    try:
        num1 = float(text1.get())
        num2 = float(text2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Ошибка"
            else:
                result = num1 / num2
        else:
            result = "Ошибка"

        result1.config(text=f"{result}")
    except ValueError:
        result1.config(text="Ошибка")


root = tk.Tk()
root.title("Калькулятор")

text1 = tk.Entry(root)
text1.grid(row=0)
text2 = tk.Entry(root)
text2.grid(row=1)
result1 = tk.Label(root, text="Результат:")
result1.grid(row=7, pady=10)
add_btn = tk.Button(root, text="+", width=10, command=lambda: calculate("+"))
add_btn.grid(row=3, pady=5)
sub_btn = tk.Button(root, text="-", width=10, command=lambda: calculate("-"))
sub_btn.grid(row=4, pady=5)
mul_btn = tk.Button(root, text="*", width=10, command=lambda: calculate("*"))
mul_btn.grid(row=5, pady=5)
div_btn = tk.Button(root, text="/", width=10, command=lambda: calculate("/"))
div_btn.grid(row=6, pady=5)

root.mainloop()
