import tkinter as tk

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
text = tk.Text(root, height=1, width=30)
text.pack(pady=5)
text.tag_configure("centered", justify="center")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
colors = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00",
          "#007dff", "#0000ff", "#7d00ff"]
for color in colors:
    btn = tk.Button(btn_frame, bg=color, width=5, height=2,
                    command=lambda c=color: button_click(c))
    btn.pack(side=tk.LEFT, padx=2)

root.mainloop()
