# def letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 85:
#         return 'A'
#     elif n > 79:
#         return 'A-'

#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         sign = "-"
#     elif ones > 6:
#         sign = "+"
#     else:
#         sign = ""
#     return "DCB"[tens - 5] + sign


# print(letter_grade(52))
# print(letter_grade(67))
# print(letter_grade(65))

'''
[]  -> True
[-5, 10, 99, 123456] -> True
[2, 3, 3, 4, 5] ->  False
[-99] -> True
[4, 5, 6, 7, 3, 7, 9] ->  False
[1, 1, 1, 1] -> False
'''


# def riffle(items: list, out=True) -> list:
#     pass


# # input : [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4][5, 6, 7, 8]
# # output:
# # out = True
# [1, 5, 2, 6, 3, 7, 4, 8]
# # out = False
# [5, 1, 6, 2, 7, 3, 8, 4]
# '''________________________________________________'''
# riffle([1, 2, 3, 4, 5, 6, 7, 8], True)  # [1,5,2,6,3,7,4,8]
# riffle([1, 2, 3, 4, 5, 6, 7, 8], False)  # [5,1,6,2,7,3,8,4]
# riffle([], True)  # []
# riffle(['bob', 'jack'], True)  # ['bob','jack']
# riffle(['bob', 'jack'], False)  # ['jack','bob']

# Unpacking

# letters = ['a', 'b', 'c', 'd', 'a', 'b', 'c',
#            'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
# a = letters[0]
# b = letters[1]
# c = letters[2]
# d = letters[3]
# a, b, c, d = letters
# print(a, b, c, d)

# a,b,*others = letters
# print(a,b,others)
# a,*others,last = letters
# print(a,last)

# for item in enumerate(letters):
#     print(item)
# for index,value in enumerate(letters):
#     print(f'number {index} is {value}')

# print(letters.count('c'))


# def custom_count(items, item):
#     items = list(items)
#     counter = 0
#     for val in items:
#         if val == item:
#             counter += 1
#     return counter


# print(custom_count(letters, 'c'))

# numbers = [1, 2, 13, 14, 5]
# numbers.sort()
# print(numbers)
# new_numbers = sorted(numbers)
# print(new_numbers)
# new_numbers = sorted(numbers,reverse=True)
# print(new_numbers)

# letters.sort(reverse=True)
# print(letters)

# print(ord('a'))
# print(ord('b'))


# products = [("product_one", 10), ("product_two", 9), ("product_three", 50)]
# print(sorted(products))


# def sort_item(item):
#     return item[1]


# products.sort(key=sort_item)
# print(products)


# def apply_to_each(L, F):
#     for i in range(len(L)):
#         L[i] = F(L[i])
#     return L


# print(apply_to_each([1, -2, 3], abs))
# print(apply_to_each([1, -2, 3.2], int))
# print(apply_to_each([1, -2, 3], float))

# def applyFuncs(L, x):
#     for f in L:
#         print(f(x))


# applyFuncs([abs, int, float], 4)


# x = map(abs, [-1, -2, 1])
# print(list(x))
# for item in x :
#     print(item)

# l1 = [1,12,15]
# l2 = [2,11,35]
# x = map(min, l1,l2)
# print(list(x))


# import test
# from test import greet, NUMBER
# from test import greet, PI

# Pi = 3.2


# def greeting():
#     pass


# message = test.greet("nikan")
# message = greet("nikan")
# print(message)
# print(PI)

# import test as t
# from test import area as a
# t.greet("")
# a()


import calendar as cal
import time
import datetime
print(cal.day_name[cal.weekday(2022, 12, 8)])
