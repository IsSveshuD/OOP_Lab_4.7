import tkinter as tk

"""
Решите задачу: напишите программу, состоящую из семи кнопок,
цвета которых соответствуют цветам радуги. При нажатии на ту
или иную кнопку в текстовое поле должен вставляться код цвета,
а в метку – название цвета. Коды цветов в шестнадцатеричной
кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 –
желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий,
#7d00ff – фиолетовый.
"""

color_codes = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зелёный",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}


def button_click(color_code):
    col_label.config(text=color_codes[color_code])
    text.delete(1.0, tk.END)
    text.insert(tk.END, color_code, "centered")


root = tk.Tk()
root.title("Цвета радуги")
col_label = tk.Label(root)
col_label.pack(pady=5)
text = tk.Text(root, height=1, width=15)
text.pack(pady=5)
text.tag_configure("centered", justify="center")

colors = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00",
          "#007dff", "#0000ff", "#7d00ff"]
for color in colors:
    btn = tk.Button(root, bg=color, width=15, height=2,
                    command=lambda c=color: button_click(c))
    btn.pack(pady=2)

root.mainloop()
