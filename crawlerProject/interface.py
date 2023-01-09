# GUI Graphic User Interface
import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello")
    my_label.config(text="سلام")


root = tk.Tk()
root.geometry("400x600")
root.resizable(False, False)
root.title('my app')
root.iconbitmap('./crawlerProject/images/orange.ico')


# my_label = ttk.Label(root, text="Hello every body", padding=20) # padding all sides
# my_label = ttk.Label(root, text="Hello every body", padding=(
#     20, 50))  # padding left/right and top/bottom
my_label = ttk.Label(root, text="Hello every body",
                     background="silver", padding=(20, 50, 10, 100))
my_label.pack(fill="both", expand=True)


greet_button = ttk.Button(
    root, text="سلام",  padding=10, command=greet)

greet_button.pack(side="left", fill="both", expand=True)
greet_button = ttk.Button(root, text="خروج", padding=10,
                          command=root.quit)

greet_button.pack(side="left", fill="both", expand=True)
greet_button = ttk.Button(root, text="خروج", padding=10, command=root.quit)

greet_button.pack(side="left", fill="both", expand=True)


root.mainloop()
# print("END")
