# GUI Graphic User Interface
import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello")
    my_label.config(text="سلام")


root = tk.Tk()
style = ttk.Style(root)
style.configure("TButton", foreground="pink")
print(style.layout("TButton"))
print(style.element_options("Button.label"))


# my_label = ttk.Label(root, text="Hello every body", padding=20) # padding all sides
# my_label = ttk.Label(root, text="Hello every body", padding=(
#     20, 50))  # padding left/right and top/bottom
my_label = ttk.Label(root, text="Hello every body",
                     background="silver", padding=(20, 50, 10, 100))
my_label.pack(fill="x")


greet_button = ttk.Button(
    root, text="سلام",  padding=10, command=greet)

greet_button.pack(side="left", fill="y")
greet_button = ttk.Button(root, text="خروج", padding=10,
                          command=root.quit)

greet_button.pack(side="left", fill="y")
greet_button = ttk.Button(root, text="خروج", padding=10, command=root.quit)

greet_button.pack(side="left", fill="y")


root.mainloop()
# print("END")
