# about tkinter widgets

# about label widget

import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

root = tk.Tk()
style = ttk.Style('flatly')
root.geometry("600x400+400+100")
root.resizable(False, False)
root.title("my app")
# root.iconbitmap("images/orange.ico")
# root.columnconfigure(0, weight=1)

# # adding Image to Label
# image = Image.open("images/orange.ico")
# photo = ImageTk.PhotoImage(image)

# # adding label
# label = ttk.Label(root, text="Hello", padding=20,
#                   image=photo, compound="right")  # compound = "right" , "left", "center", "top","bottom"
# label.config(font=("Hevetica", 20), border=4,
#              background="cyan", relief="solid")
# label.grid(row=0, column=0)
# # text widget
# text = tk.Text(root, height=9)
# text.grid(row=1, column=0)
# text.insert(1.0, "bbbbbbbbbbbbbbbbbb")
# text.insert(1.2, "aaaa")
# text_content = text.get("1.0", "end")
# print(text_content)

# # scrollbar
# text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# text_scroll.grid(row=1, column=1, sticky="ns")
# text["yscrollcommand"] = text_scroll.set

# # seprator widget
# separator = ttk.Separator(root, orient="horizontal")
# separator.grid(row=2, column=0, pady=10, sticky="ew")
# second_label = ttk.Label(root, text="number two")
# second_label.grid(row=3, column=0)

# check button


# def do_some_thing():
#     print(check_option_val.get())


# check_option_val = tk.IntVar()
# check_button = ttk.Checkbutton(
#     root, text="some thing", command=do_some_thing, onvalue=1, offvalue=0, variable=check_option_val)
# check_button.pack()


# radio button a group of items which we can select only one of them
# def selection():
#     print(storage_variable.get())


# storage_variable = tk.StringVar()
# option_one = ttk.Radiobutton(
#     root, text="Female", value="Female", variable=storage_variable, command=selection, bootstyle="success")
# option_one.grid(row=0, column=0, padx=0, pady=10, sticky="w")
# option_two = ttk.Radiobutton(
#     root, text="Male", value="Male", variable=storage_variable, command=selection, bootstyle="success")

# option_two.grid(row=1, column=0, padx=0, pady=10, sticky="w")

# combobox widget

weekday = tk.StringVar(value="select a day... ")
weekday_combobox = ttk.Combobox(
    root, textvariable=weekday, bootstyle="danger")
weekday_combobox.pack(fill="both")
weekday_combobox["values"] = (
    "Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun")

root.mainloop()
