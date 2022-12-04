# def greet():
# local scope
# message = "hi"


# greet()
# print(message)


# global scope

counter = 0


# def greet():
#     global counter
#     counter += 1


# greet()
# greet()
# greet()
# print(counter)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print("start")
print(multiply(1,2,3))