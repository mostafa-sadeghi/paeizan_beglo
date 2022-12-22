from timeit import timeit
code1 = """
def calc(age):
    if age <= 0:
        raise ValueError('Age can not be negative')

    return 10/age

try:
    calc(-1)
except ValueError as error:
    print('error')
"""
# print(timeit(code1, number=1000))

code2 = """
def calc(age):
    if age <= 0:
        return None

    return 10/age

try:
    calc(-1)
except ValueError as error:
    print('error')
"""
# print(timeit(code2, number=1000))


# def calc(age):
#     if age <= 0:
#         raise ValueError('Age can not be negative')

#     return 10/age


# calc(-1)


# OOP Object Oriented
# x = 1
# print(type(x))

# class Point:
#     # method:
#     def draw(self):
#         print('draw')


# instance
# p1 = Point()
# print(type(p1))
# print(isinstance(p1, Point))


# class Animate:
#     def live(self):
#         print('live')

#     def move(self):
#         print('move')

#     def eat(self):
#         print('eat')


# mammal = Animate()
# mammal.live()
# mammal.move()


# class Car:
#     def move(self):
#         print('move')

#     def change_speed(self):
#         print('change speed')


# bmw = Car()
# nissan = Car()


# class Point:
#     # class level attribute
#     color = "black"
#     def __init__(self, x: int, y: int) -> None:
#         # instance level attribute
#         self.x = x
#         self.y = y

#     # instance method:

#     def draw(self):
#         print('draw')

#     @classmethod
#     def zero(cls):
#         return cls(0,0)


# point = Point.zero() #
# print(point.x)


# p1 = Point(1, 2)  # Point(p1,1,2)
# # p1.z = 12
# # p1.draw()  # Point.draw(p1)
# # print(p1.x)
# # print(p1.y)
# p2 = Point(3, 4)  # Point(p2,3,4)
# # print(p2.x)
# # print(p2.y)
# p1.color = 'red'
# print(p1.color)
# print(p2.color)
# print(Point.color)

# class Human:
#     color = 'red'
#     def __init__(self, name):
#         self.name = name
#     def method(self):
#         return 'instance method called', self
#     def get_name(self):
#         return self.name
#     def set_name(self, name):
#         self.name = name
#     @classmethod
#     def classmethod(cls):
#         cls.color = 'green'
#         return 'class method called', cls
#     @staticmethod
#     def staticmethod():
#         print('bakaala')
#         return 'static method called'
#     def __repr__(self):
#         return self.name
#     def __str__(self):
#         return self.name
# h1 = Human("ali")
# print(h1)
# print(str(h1))


# print(h1.name)
# h1.color = 'black'
# Human.classmethod()
# h2 = Human('name')
# print(h1.color)
# print(h2.color)
# h1.staticmethod()

# h1.set_name('tina')
# print(h1.get_name())


# c = MyClass.classmethod()
# print(MyClass.color)
# p = MyClass()
# print(p.color)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __gt__(self, o):
        return self.x > o.x and self.y > o.y

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
# p1 = Point(11, 12)
# p2 = Point(1, 2)

# print(p1 > p2)
p = p1 + p2
print(p1 + p2)
print(p)
