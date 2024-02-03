import tkinter as tk

"""
Напишите программу, в которой имеется несколько объединенных
в группу радиокнопок, индикатор которых выключен ( indicatoron=0 ).
Если какая-нибудь кнопка включается, то в метке должна отображаться
соответствующая ей информация. Обычных кнопок в окне быть
не должно.
"""


def update_label():
    selected_option = var.get()
    label.config(text=f"{selected_option}")


root = tk.Tk()
root.title("Кнопки")

var = tk.StringVar()
radio_btn_1 = tk.Radiobutton(root, text="Вася", width=10,
                             height=3, variable=var, value="Рыбы",
                             indicatoron=False, command=update_label)
radio_btn_2 = tk.Radiobutton(root, text="Дина", width=10,
                             height=3, variable=var, value="Козерог",
                             indicatoron=False, command=update_label)
radio_btn_3 = tk.Radiobutton(root, text="Лиза", width=10,
                             height=3, variable=var, value="Весы",
                             indicatoron=False, command=update_label)

label = tk.Label(root, width=20, anchor="center")
label.grid(row=0, column=1, rowspan=3, sticky="w")
radio_btn_1.grid(row=0, column=0, sticky="w")
radio_btn_2.grid(row=1, column=0, sticky="w")
radio_btn_3.grid(row=2, column=0, sticky="w")

root.mainloop()
