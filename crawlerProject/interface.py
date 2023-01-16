# GUI Graphic User Interface
import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello")
    my_label.config(text="سلام")


root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title('my app')
root.iconbitmap('./crawlerProject/images/orange.ico')


root.mainloop()
# print("END")
