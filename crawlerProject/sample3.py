# https://ttkbootstrap.readthedocs.io/en/latest/

import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb

root = ttkb.Window(themename="superhero")
my_style = ttkb.Style()
my_style.configure("TButton", font=("Helvetica", 18))

my_label = ttkb.Label(text="Hello every body", font=(
    "Arial", 28), bootstyle="danger")
my_label.pack(pady=10)

my_button = ttkb.Button(
    text="Click me!", bootstyle="success, outline", width=20)
my_button.pack(pady=10)


# check button
def check_command():
    if check_button_var.get() == 1:
        my_label.config(text="checked!")
    else:
        my_label.config(text="Unchecked!")


check_button_var = tk.IntVar()

my_check = ttkb.Checkbutton(text="check me", bootstyle="primary",
                            onvalue=1, offvalue=0, variable=check_button_var, command=check_command)
my_check.pack(pady=10)
# tool button
check_button_var3 = tk.IntVar()
my_check3 = ttkb.Checkbutton(text="check me3", bootstyle="danger, toolbutton",
                             onvalue=1, offvalue=0, variable=check_button_var3, command=check_command)
my_check3.pack(pady=10)
# round toggle
check_button_var1 = tk.IntVar()
my_check2 = ttkb.Checkbutton(text="check me2", bootstyle="success, round-toggle",
                             onvalue=1, offvalue=0, variable=check_button_var1, command=check_command)
my_check2.pack(pady=10)
# square round toggle
check_button_var4 = tk.IntVar()
my_check4 = ttkb.Checkbutton(text="check me4", bootstyle="success, square-toggle",
                             onvalue=1, offvalue=0, variable=check_button_var4, command=check_command)
my_check4.pack(pady=10)


root.mainloop()
