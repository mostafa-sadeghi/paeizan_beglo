import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
style = ttk.Style('darkly')
# input frame -> label + entrybox
input_frame = ttk.Frame(root, border=4, relief="solid")
input_frame.grid(row=0, column=0, sticky="news")
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
input_frame.rowconfigure(0, weight=1)


user_name_label = ttk.Label(input_frame, text="user name", anchor="center")
user_name_label.grid(row=0, column=0, padx=(0, 30), sticky="eswn")

user_name_entry = ttk.Entry(input_frame, bootstyle="primary")
user_name_entry.grid(row=0, column=1, sticky="eswn")

# buttons frame -> greet button + quit button
buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=1, column=0, sticky="ewns")

buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
buttons_frame.rowconfigure(0, weight=1)

button_greet = ttk.Button(buttons_frame, text="greet",
                          bootstyle="success, outline")
button_greet.grid(column=0, row=0, sticky="ewns")
quit_greet = ttk.Button(buttons_frame, text="quit")
quit_greet.grid(column=1, row=0, sticky="ewns")


root.mainloop()
