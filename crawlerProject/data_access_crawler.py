# todo

import sqlite3
import tkinter as tk
from tkinter import ttk, END
conn = sqlite3.connect('address_book.db')
c = conn.cursor()
# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text

# )
# """)


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # insert into db
    sql = """INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city)
    """
    c.execute(sql, {'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    })
    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    sql = """SELECT *,oid FROM addresses"""
    c.execute(sql)
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " "+str(record[1]) + "\n"

    query_label = ttk.Label(root, text=print_records)
    query_label.grid(row=6, column=0, columnspan=2)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    sql = "DELETE FROM addresses WHERE oid= " + delete_box.get()
    c.execute(sql)
    conn.commit()
    conn.close()


def edit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    sql = """UPDATE addresses SET 
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    """


def update():
    editor = tk.Tk()
    editor.title('Update a record')
    editor.geometry('400x600')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    sql = """SELECT * FROM addresses WHERE oid= """ + record_id
    c.execute(sql)
    records = c.fetchall()

    f_name = tk.Entry(editor, width=30)
    f_name.grid(row=0, column=1, padx=20)

    # create entry boxes
    l_name = tk.Entry(editor, width=30)
    l_name.grid(row=1, column=1, padx=20)
    address = tk.Entry(editor, width=30)
    address.grid(row=2, column=1, padx=20)
    city = tk.Entry(editor, width=30)
    city.grid(row=3, column=1, padx=20)

    # create labels
    f_name_label = ttk.Label(editor, text="first name")
    f_name_label.grid(row=0, column=0, padx=20)
    l_name_label = ttk.Label(editor, text="last name")
    l_name_label.grid(row=1, column=0, padx=20)
    address_label = ttk.Label(editor, text="address", anchor='w', width=10)
    address_label.grid(row=2, column=0, padx=20)
    city_label = ttk.Label(editor, text="city")
    city_label.grid(row=3, column=0, padx=20)

    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])

    # submit button
    edit_button = ttk.Button(editor, text="Add record to db", command=edit)
    edit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


root = tk.Tk()
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

# create entry boxes
l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

# create labels
f_name_label = ttk.Label(root, text="first name")
f_name_label.grid(row=0, column=0, padx=20)
l_name_label = ttk.Label(root, text="last name")
l_name_label.grid(row=1, column=0, padx=20)
address_label = ttk.Label(root, text="address", anchor='w', width=10)
address_label.grid(row=2, column=0, padx=20)
city_label = ttk.Label(root, text="city")
city_label.grid(row=3, column=0, padx=20)

# submit button
submit_button = ttk.Button(root, text="Add record to db", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# delete entry box
delete_box = tk.Entry(root, width=30)
delete_box.grid(row=7, column=1)

delete_box_label = ttk.Label(root, text="ID #")
delete_box_label.grid(row=7, column=0)
# delete button
delete_button = ttk.Button(root, text="delete item", command=delete)
delete_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# create query_button
query_button = ttk.Button(root, text="show records", command=query)
query_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# update button
update_button = ttk.Button(root, text="update item", command=update)
update_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
