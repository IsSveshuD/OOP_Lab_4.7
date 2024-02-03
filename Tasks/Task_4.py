import tkinter as tk
from tkinter import messagebox
import os

"""
Решите задачу: напишите программу, состоящую из однострочного и
многострочного текстовых полей и двух кнопок "Открыть" и "Сохранить".
При клике на первую должен открываться на чтение файл, чье имя указано
в поле класса Entry , а содержимое файла должно загружаться в поле
типа Text . При клике на вторую кнопку текст, введенный пользователем
в экземпляр Text , должен сохраняться в файле под именем, которое
пользователь указал в однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл
скрипта, если указывать имена файлов без адреса.
"""


class FileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        self.filename = tk.Entry(root, width=40)
        self.filename.grid(row=0, column=0, padx=5, pady=5)

        open_btn = tk.Button(root, text="Открыть", command=self.open_file)
        open_btn.grid(row=0, column=1, padx=5, pady=5)

        save_btn = tk.Button(root, text="Сохранить", command=self.save_file)
        save_btn.grid(row=0, column=2, padx=5, pady=5)

        self.text_editor = tk.Text(root, height=10, width=50)
        self.text_editor.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def open_file(self):
        filename = self.filename.get()
        try:
            with open(os.path.join(os.path.dirname(__file__),
                                   filename), 'r') as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл не найден")

    def save_file(self):
        filename = self.filename.get()
        filepath = os.path.join(os.path.dirname(__file__), filename)
        content = self.text_editor.get(1.0, tk.END)
        with open(filepath, 'w') as file:
            file.write(content)
        messagebox.showinfo("Результат", "Файл сохранен")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditor(root)
    root.mainloop()
