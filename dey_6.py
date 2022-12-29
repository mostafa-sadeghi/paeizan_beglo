# inheritance   وراثت یا ارث بری


# class Mammal:
#     def eat(self):
#         print("eat")

#     def walk(self):
#         print("walk")


# class Fish:
#     def eat(self):
#         print("eat")

#     def swim(self):
#         print(self)


# DRY dont repeat yourself

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):

#     def __init__(self):
#         super().__init__()
#         self.weight = 5

#     def walk(self):
#         print("walk")


# class Fish(Animal):

#     def swim(self):
#         print(self)


# cow = Mammal()
# cow.walk()
# cow.eat()

# print(cow.weight)
# print(cow.age)

# print(isinstance(cow, Mammal))
# print(isinstance(cow, Animal))
# print(issubclass(Mammal, Animal))
