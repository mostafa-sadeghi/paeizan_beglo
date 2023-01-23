# from array import array
# list
# my_list = [1, 's', 'aaaa']

# array
# x = array('i', [1, 2, 3])
# print(x[0])

# numpy matplotlib pillow

import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


def graph():
    prices = np.random.normal(2_000_000, 2_400_000, 5000)
    plt.hist(prices, 40)
    plt.show()


root = tk.Tk()
my_button = tk.Button(root, text="show graph", command=graph)
my_button.pack()

root.mainloop()
