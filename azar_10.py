# def max_(l):
#     float_list = []
#     for item in l:
#         if type(item) == float:
#             float_list.append(item)
#     if len(float_list) == 0:
#         return f'Nothing'
#     return max(float_list)


# x = max_([100, 'blue', 3.5, 'sugar on the rocks', 7.0])
# x = max_([100, 10])
# print(x)

# def max(l):
#     max_float = 0
#     for item in l:
#         if isinstance(item, float):
#             if item > max_float:
#                 max_float = item
#     if max_float == 0:
#         return f'Nothing'
#     return max_float


# x1 = max([100, 'blue', 3.5, 'sugar on the rocks', 7.0])
# x2 = max([100, 10])
# print(x1, x2)

'''[] ->True

[9] -> True
[-5, 9, 11] -> True
[-5, 9, 9, 11] -> False
[2,3,5,4] -> False


'''

# numbers = list(range(1, 101))
# print(numbers)
# numbers = tuple(range(1, 101))
# print(numbers)

# # list comprehension

# numbers = [x for x in range(1000)]
# print(numbers)
# numbers = [x for x in range(1000) if x % 2 == 0]
# print(numbers)

# numbers = []
# for i in range(1000):
#     if i % 2 == 0:
#         numbers.append(i)

from math import sqrt


def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def p(points):
    result = 0
    for i in range(len(points)-1):
        result += distance(points[i], points[i+1])
    else:
        result += distance(points[0], points[-1])
    return result


x = p([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
print(x)
