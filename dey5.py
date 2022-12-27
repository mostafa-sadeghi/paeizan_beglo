# private
# access level
# class Point:
#     # __color = "red"  # private
#     def __init__(self):
#         self.__color = "red"


# print(Point.__color)
# print(Point._Point__color)
# print(Point.__dict__)

# point = Point()
# # print(point.color)
# print(point._Point__color)
# print(point.__dict__)

# class Product:
#     def __init__(self, name, price):
#         # self.set_price(price)
#         self.price = price

# def get_price(self):
#     return self.__price
# @property
# def price(self):
#     return self.__price

# def set_price(self, value):
#     if value < 0:
#         raise ValueError('Price can not be begative')
#     self.__price = value

# @price.setter
# def price(self, value):
#     if value < 0:
#         raise ValueError('Price can not be begative')
#     self.__price = value

# price = property(get_price, set_price)


# product = Product("pro1", 20)
# print(product.price)
# product.price = 300
# print(product.price)


# print(product.price)

# print(product.price)
# product.price = 100
# print(product.price)

# product.set_price(120)


# product.set_price(200)
# print(product.get_price())

# p2 = Product("p2", -20)
# print(p2.price)
