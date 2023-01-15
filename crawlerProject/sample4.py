# how to use grid for adding/putting widgets on the screen

import tkinter as tk
from tkinter import ttk

import ttkbootstrap as ttkb

root = ttkb.Window(themename="superhero")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# adding frame
main_frame = ttkb.LabelFrame(text="user info", bootstyle="info")
main_frame.grid(row=0, column=0, sticky="ewns")
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)


# adding label
child_frame_1 = ttk.Frame(main_frame)
child_frame_1.grid(column=0, row=0, sticky="ewns")
child_frame_1.columnconfigure(0, weight=1)
child_frame_1.columnconfigure(1, weight=1)
child_frame_1.rowconfigure(0, weight=1)


name_label = ttkb.Label(child_frame_1, text="name",
                        bootstyle="primary", font=12)
name_label.grid(row=0, column=0, padx=(0, 15), pady=10, sticky="ewns")

# adding entry
name_entry = ttkb.Entry(child_frame_1, bootstyle="danger")
name_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="ewns")
name_entry.focus()

# # adding buttons
# child_frame_2 = ttk.Frame(main_frame)
# child_frame_2.grid(column=0, row=1)
# child_frame_2.columnconfigure(0, weight=1)
# child_frame_2.columnconfigure(1, weight=1)
# greet_button = ttkb.Button(child_frame_2, text="greet",
#                            bootstyle="success, outline")
# greet_button.grid(row=1, column=0, pady=10, sticky="ew")
# quit_button = ttkb.Button(child_frame_2, text="quit",
#                           bootstyle="danger, outline")
# quit_button.grid(row=1, column=1, pady=10, sticky="ew")

root.mainloop()
