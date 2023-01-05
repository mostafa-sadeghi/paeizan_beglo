import sqlite3
from pathlib import Path
import shutil

# source = Path("f.txt")
# destination = Path('f_copy.txt')
# destination.write_text('')

# shutil.copy(source, destination)

# zip files:

# from zipfile import ZipFile
# creating a zip file
# with ZipFile("sample1.zip", "w") as zip:
#     for path in Path("sample").rglob("*.*"):
#         zip.write(path)
# listing files in the zipped file
# with ZipFile("sample1.zip") as zip:
# files = zip.namelist()
# # print(files)
# for file in files:
#     path = Path(file)
#     print(path.read_text())
# extracting a zip file
# zip.extractall("newDIR")

# csv comma seprated
# import csv
# file = open("data.csv", "w")
# file.close()

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
# writer.writerow([1001, 1, 12])
# writer.writerow([1002, 2, 45])
# writer.writerows([[1002, 2, 45], [1002, 2, 45]])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     print(list(reader))


# JSON javascript object notation

# with open("f.txt") as file:
#     all_data = file.readlines()
#     for data in all_data:
#         print(data.split(' '))
import json
from pathlib import Path

# movies = [
#     {
#         'id': 1,
#         'name': 'terminator1',
#         'year': 1998
#     },
#     {
#         'id': 2,
#         'name': 'terminator2',
#         'year': 2002
#     },
# ]
# create json string from our list
# data = json.dumps(movies)
# print(data)
# print(type(data))
# create json file and wrote json string in it.
# Path('movies.json').write_text(data)

# read data from json file
# data = Path('movies.json').read_text()
# convert json text to python object
# movies = json.loads(data)
# print(movies)
# print(movies[0])
# print(movies[0]['name'])
# print(f"{'id':<4}{'name':<16}{'year':>6} ")
# for movie in movies:
#     print(f"{movie['id']:<4}{movie['name']:>16}{movie['year']:>6} ")

# database
# DBMS = database management system
# data base Types:
# relational databases = Table -> structured: sqlite, mysql, postgresql, maridb, sqlserver
# nosql non relational = unstructured -> bigdata : mongodb


data = Path('movies.json').read_text()
movies = json.loads(data)
for movie in movies:
    print(movie)

# connection = sqlite3.connect("my_db.sqlite3")
# better way:


def open_connection():
    with sqlite3.connect("my_db.sqlite3") as conn:
        return conn


def create_table():
    conn = open_connection()

    sql_query = """CREATE Table IF NOT EXISTS movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name text,
        year text
    )
    """
    cursor = conn.cursor()
    cursor.execute(sql_query)
    conn.commit()
    conn.close()


def insert_into_db_from_file():
    conn = open_connection()
    cursor = conn.cursor()
    sql_query_insert = "INSERT INTO movies(name,year) VALUES(:name,:year)"

    for movie in movies:
        cursor.execute(sql_query_insert, {
            'name': movie['name'],
            'year': movie['year']
        })
    conn.commit()
    conn.close()


def insert_into_db(name, year):
    conn = open_connection()
    cursor = conn.cursor()
    sql_query_insert = "INSERT INTO movies(name,year) VALUES(:name,:year)"
    cursor.execute(sql_query_insert, {
        'name': name,
        'year': year
    })

    conn.commit()
    conn.close()


def select_all_data():
    conn = open_connection()
    cursor = conn.cursor()
    sql_query_select = "SELECT * FROM movies"
    cursor.execute(sql_query_select)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data
