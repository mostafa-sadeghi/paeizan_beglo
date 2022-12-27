
# try:
#     f = open("f.txt", 'r')
#     a = int(input('> '))
#     b = int(input('> '))
#     c = a/b
#     print(c)


# except (ZeroDivisionError, FileNotFoundError):
#     print('ZeroDivisionError occured | FileNotFoundError')
# except ValueError:
#     print('ValueError')
# else:
#     print('No Exception')
# finally:
#     print('finally')
#     f.close()

# print("ok")


# lambda
# def get_price(item):
#     return item[1]


products = [('produc1', 100), ('p2', 200), ('p3', 150)]
# products.sort(key=get_price)
# new_products =  sorted(products, key=get_price)
# print(products)
# products.sort(key=lambda item: item[1])
# print(products)


# x = (lambda x, y: x+y)(2, 3)
# print(x)


# def x(x, y): return x+y


# print(x(2, 2))


# def square(x):
#     return x**2


# def apply_(f, x):
#     print(f(x))


# apply_(square, 2)

# apply_(lambda x: x*2, 4)

# def my_func(l, f):
#     for i in l:
#         print(f(i))


# my_func([1, -2, 3], abs)


# def my_func(l, x):
#     for f in l:
#         print(f(x))


# my_func([int, float, abs], -1.8)

# map function
products = [('produc1', 100), ('p2', 200), ('p3', 150)]
# prices = []
# for product in products:
#     prices.append(product[1])

# print(prices)

# prices_map = map(lambda x: x[1], products)
# # print(list(prices_map))
# for item in prices_map:
#     print(item)


# my = map(lambda x: x[1] > 100, products)
# print(list(my))

# filter
# temp = filter(lambda x: x[1] > 100, products)
# print(list(temp))

# list comprehension

# products = [('produc1', 100), ('p2', 200), ('p3', 150)]
# prices = [item[1] for item in products]
# print(prices)
# prices_greater_ = [item for item in products if item[1] > 100]
# print(prices_greater_)

# zip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# output = [(1,'a'),(2,'b'),(3,'c')]
# output = zip(list1, list2)
# print(list(output))

# output = []
# for i in range(len(list1)):
#     temp = tuple()
#     temp += (list1[i],)
#     temp += (list2[i],)
#     output.append(temp)
# print(output)
