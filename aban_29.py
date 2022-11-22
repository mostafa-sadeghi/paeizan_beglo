# val = 3
# grade = 19

# string = "hello student number %s your grade is: %s" % (val, grade)
# string = f"hello student number {val} your grade is: {grade}"
# print(string)


# x = input('> ')

# # a1 = f'{x}'
# a1 = '%s' % x
# # a2 = f'{x}{x}'
# a2 = '%s%s' % (x, x)
# # a3 = f'{x}{x}{x}'
# a3 = '%s%s%s' % (x, x, x)

# result = int(a1) + int(a2) + int(a3)
# print(f'{a1} + {a2} + {a3} = {result}')

# کلمات کلیدی pass، continue، break
# a = 1
# if a > 5:
#     pass

# for i in range(8):
#     if i == 6:
#         break
#     print(i)

# for i in range(8):
#     if i == 6:
#         continue
#     print(i)

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

# else:
#     print('end')
# for i in range(10):
#     print(i)


# print('end')


# sample of for else:
# success = False
# counter = 3

# for number in range(counter):
#     print("attempt")

#     if success == True:
#         print("success")
#         break
# else:
#     print("attempted 3 times and failed")


# Tuple datatype

# numbers = (1, 2, 3, 4, 5)
# print(type(numbers))
# for number in numbers:
#     print(number)
# print(numbers[0])
# print(numbers[:3])
# tupple is immutable
# numbers[0] = 10

# dictionary:
# students_favorite = {
#     'ali': 'footbal',
#     'reza': 'baseball',
#     'mina': 'tennis'
# }

# print(f'mina likes : {students_favorite["mina"]}')
# تغییر در دیکشنری
# students_favorite['mina'] = 'volleyball'
# print(students_favorite)
# students_favorite['nasrin'] = 'basketball'
# print(students_favorite)
# del students_favorite['ali']
# print(students_favorite)

# print(students_favorite.keys())
# print(students_favorite.values())

students_favorite = {
    'ali': 'footbal',
    'reza': 'baseball',
    'mina': 'tennis'
}
# for item in students_favorite:
#     print(item)

# for value in students_favorite.values():
#     print(value)

# for item in students_favorite.items():
#     print(item)
# for key, value in students_favorite.items():
#     print(key, value)

