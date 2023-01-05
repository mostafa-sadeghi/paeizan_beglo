from data_access_layer import insert_into_db, select_all_data
print('''This app is used for store and retreiving movies
to add movie enter 1
to show all movies enter 2
''')


def show_table(movies):
    for movie in movies:
        print(f'{str(movie[0]):^6}{str(movie[1]):^32}{str(movie[2]):^6}')


while True:
    print('To exit enter 0')
    entry = input('> ')
    if entry == "0":
        exit()
    elif entry == "1":
        movie_name = input("enter your favorite movie's name ")
        movies_year = input("enter release year")
        insert_into_db(movie_name, movies_year)

    elif entry == "2":
        movies = select_all_data()
        print(f'{"id":^6}{"name":^32}{"year":^6}')
        show_table(movies)
