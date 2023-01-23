import tkinter as tk
from tkinter import ttk, END
import mysql.connector


def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    email_box.delete(0, END)
    username_box.delete(0, END)
    price_paid_box.delete(0, END)


def add_customer():
    pass


root = tk.Tk()

# connect to db
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="1qaz!QAZ", database="niklearning")

my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE niklearning")
print(mydb)

# create labels
title_label = ttk.Label(root, text="some thing", font=15)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# create main frame
# adding labels
first_label = ttk.Label(root, text="first name", font=15)
first_label.grid(row=1, column=0, sticky='w', padx=10)
last_label = ttk.Label(root, text="last name", font=15)
last_label.grid(row=2, column=0, sticky='w', padx=10)
address1_label = ttk.Label(root, text="address1", font=15)
address1_label.grid(row=3, column=0, sticky='w', padx=10)
address2_label = ttk.Label(root, text="address2", font=15)
address2_label.grid(row=4, column=0, sticky='w', padx=10)
city_label = ttk.Label(root, text="city", font=15)
city_label.grid(row=5, column=0, sticky='w', padx=10)
phone_label = ttk.Label(root, text="phone", font=15)
phone_label.grid(row=6, column=0, sticky='w', padx=10)
email_label = ttk.Label(root, text="email", font=15)
email_label.grid(row=7, column=0, sticky='w', padx=10)
username_label = ttk.Label(root, text="username", font=15)
username_label.grid(row=8, column=0, sticky='w', padx=10)
price_paid_label = ttk.Label(root, text="price paid", font=15)
price_paid_label.grid(row=9, column=0, sticky='w', padx=10)
# adding entry boxes

first_name_box = ttk.Entry(root)
first_name_box.grid(row=1, column=1)
last_name_box = ttk.Entry(root)
last_name_box.grid(row=2, column=1, pady=5)
address1_box = ttk.Entry(root)
address1_box.grid(row=3, column=1, pady=5)
address2_box = ttk.Entry(root)
address2_box.grid(row=4, column=1, pady=5)
city_box = ttk.Entry(root)
city_box.grid(row=5, column=1, pady=5)
phone_box = ttk.Entry(root)
phone_box.grid(row=6, column=1, pady=5)
email_box = ttk.Entry(root)
email_box.grid(row=7, column=1, pady=5)
username_box = ttk.Entry(root)
username_box.grid(row=8, column=1, pady=5)
price_paid_box = ttk.Entry(root)
price_paid_box.grid(row=9, column=1, pady=5)


# adding buttons
add_customer_button = ttk.Button(
    root, text="Add Customer", command=add_customer)
add_customer_button.grid(row=10, column=0, padx=10, pady=10)
clear_fields_button = ttk.Button(
    root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=10, column=1, padx=10, pady=10)
root.mainloop()
