# print("blalallalala")
# int float bool str list tuple set dict
# name = "ali"
# char = "a"
# char1 = 'a'
# char2 = "a"


# print(type(name))
# print(type(char))
# print(type(char1))
# print(type(char2))

# x = 1
# y = 1.0

# print(type(x))
# print(type(y))

# name = name + 1


###################################################
# section 2:
# is_old = True
# if is_old:
#     print("you are old enough")
# else:
#     print("other")


# is_old = 'Hello'
# another = 5

# if is_old and another:
#     print("ok")

# casting or convert types
# x = 1.2

# y = int(x)

# string = '1'
# string = 'a'
# string = '1.2'
# x = int(float(string))


# print(x)

# x = 1
# y = bool(x)
# print(f'output is : {y}')
# x = 0
# y = bool(x)
# print(f'output is : {y}')
# x = ''
# y = bool(x)
# print(f'output is : {y}')
# x = ' '
# y = bool(x)
# print(f'output is : {y}')


# falsy values:

# 0, '', "", (), [], {}, None


# user_name = input('enter user name: ')
# password = input('enter user name: ')

# if user_name and password:
#     print("login")

# if True:
#     print()
#     print()

# def func():
#     pass


# func()

# my_list = [
#     1, 2, 3,
#     4, 5, 6,
# ]

# terneray operator
# is_friend = True

# if is_friend:
#     print("message allowed")
# else:
#     print("not allowed")


# is_friend = True
# message = "message allowed" if is_friend else "not allowed"
# print(message)


# short circuit

# one = False
# two = True
# if one and two:
#     print('ssss')


# if two or one:
#     print('ssss')


# for s in 'hello':
#     print(s)
# x = range(4)
# print('x : ', x)
# for i in range(4):
#     print(i)

# for i in range(0, 101, 2):
#     print(i)

# counter = 0
# while counter < 101:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1


print('''welcome to our program.
 this program is a simple application.
 to exit enter 0.
 to enter value > 1
 to see the result > 2
 ''')
# numbers = []
# while True:
#     user_input = input('enter your choice: ')
#     if user_input == '0':
#         exit()
#     elif user_input == '1':
#         while True:
#             user_input = input('enter a number or "exit": ')
#             if user_input == 'exit' or not user_input.isdecimal() :
#                 break
#             numbers.append(int(user_input))
#     elif user_input == '2':
#         print(f'sum of all enterd numbers is: {sum(numbers)}')


# x = int(input('> '))
# print(type(x))
# x = x + 1

# x = input(">")

# if not x.isdecimal():
#     print("this is not a valid number")


name = "ali"
family = "rezaei"

# print("your name is ", name, family)
# print("your name is %s %s" % (name, family))
print(f'your name is {name} {family}')


# // todo define custom sum function , iterate
