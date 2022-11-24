# students = []

# status = 'CONTINUE'
# while status == 'CONTINUE':
#     student = {}
#     name = input('enter your name:> ')
#     student['name'] = name
#     family = input('enter your family:> ')
#     student['family'] = family
#     age = input('enter your age: ')
#     student['age'] = age

#     students.append(student)

#     status = input(
#         'to continue > "CONTINUE" | to exit > "EXIT" | to search > SEARCH ')
#     if status.lower() == 'search':
#         search_val = input('enter name of student: ')
#         for st in students:
#             if st['name'] == search_val:
#                 print(f"'{search_val} exists and is {st['age']} years old.")
#             else:
#                 print()
#                 print(f"{search_val} does'nt exist.")

# print(students)
# print(students[0]['name'])


# string = 'aaaa'
# print(string.upper())

# define function without parameter
# def show_name():
#     print("hello paeizan")


# show_name()

# define function with parameter
# def show_name(name):
#     print(f"hello {name}")


# print(show_name("paeizan"))
# show_name() > error

# def show_name(name):
#     return f"hello {name}"


# print(show_name("paeizan"))


# def increment(number, by=1):
#     return number + by


# print(increment(10))
# print(increment(int(input('> '))))


# xargs

# def multiply(x, y):
#     return x * y


# result = multiply(3, 4)
# print('result is : ',result)
# def multiply(*args):
#     total = 1
#     for number in args:
#         total *= number
#     return total if len(args) > 0 else 0


# result = multiply(3, 4, 5)
# print('result is : ', result)
# result = multiply()
# print('result is : ', result)

# def func(name, family):
#     print(name, family)


# func("name", "family")
# func(family="family", name="name")

# kwargs


# def save_user(**user):
#     print(user)

# save_user(id=1, name="paeizan",age="20")
