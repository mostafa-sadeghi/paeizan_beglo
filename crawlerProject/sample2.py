# GUI Graphic User Interface
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
# root.geometry("400x600")
# root.resizable(False, False)
root.title('my app')
root.iconbitmap('./crawlerProject/images/orange.ico')

# adding label
# n1 = ttk.Label(root, text="Enter your Name1", background="silver")
# n1.pack(side="left", fill="both", padx=(
#     0, 10), pady=10, expand=True)
# n2 = ttk.Label(root, text="Enter your Name2", background="#D3D3D3")
# n2.pack(side="top", fill="both", padx=(
#     0, 10), pady=10, expand=True)
# n3 = ttk.Label(root, text="Enter your Name3", background="#D3D3D3")
# n3.pack(side="left", fill="both", padx=(
#     0, 10), pady=10, expand=True)


# adding Frame:

# main_frame = ttk.Frame(root)
# main_frame.pack(side="left", anchor="n", fill="both", expand=True)

# l3 = ttk.Label(main_frame, text="Label left", background="green")
# l3.pack(side="left", expand=True, fill="both")
# l1 = ttk.Label(main_frame, text="Label top", background="orange")
# l1.pack(side="top", expand=True, fill="both")
# l2 = ttk.Label(main_frame, text="Label top", background="red")
# l2.pack(side="top", expand=True, fill="both")

# adding Entry box

# adding root_frame
root_frame = ttk.LabelFrame(root, text="input")
root_frame.pack()

# adding subframes

first_frame = ttk.Frame(root_frame)
first_frame.pack(pady=10)
name_label = ttk.Label(first_frame, text="User Name", anchor="w", width=10)
name_label.pack(side="left", padx=(0, 15))

name_entry = ttk.Entry(first_frame)
name_entry.pack(side="left")

# adding family frame
second_frame = ttk.Frame(root_frame)
second_frame.pack(pady=10)
family_label = ttk.Label(second_frame, text="Password", anchor="w", width=10)
family_label.pack(side="left", padx=(0, 15))

family_entry = ttk.Entry(second_frame)
family_entry.pack(side="left")


# adding button frame
buttons_frame = ttk.Frame(root_frame)
buttons_frame.pack(pady=10)

# adding buttons
button_greet = ttk.Button(buttons_frame, text="Greet")
button_greet.pack(side="left")
button_quit = ttk.Button(buttons_frame, text="Quit")
button_quit.pack(side="left")


root.mainloop()
