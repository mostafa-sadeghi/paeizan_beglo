# val = 3
# grade = 19

# string = "hello student number %s your grade is: %s" % (val, grade)
# string = f"hello student number {val} your grade is: {grade}"
# print(string)


x = input('> ')

# a1 = f'{x}'
a1 = '%s' % x
# a2 = f'{x}{x}'
a2 = '%s%s' % (x, x)
# a3 = f'{x}{x}{x}'
a3 = '%s%s%s' % (x, x, x)

result = int(a1) + int(a2) + int(a3)
print(f'{a1} + {a2} + {a3} = {result}')
