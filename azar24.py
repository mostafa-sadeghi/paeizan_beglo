# import math

# x = math.sqrt(4)
# print(x)
# print(math.ceil(4.2))
# print(math.floor(4.2))


x = 25
epsilon = 0.01
ans = 0
inc = 0.0001
num = 0
while abs(ans ** 2 - x) >= epsilon:
    ans += inc
    num += 1

print(ans)
print(num)

print('*****************************')

x = 4
epsilon = 0.01
low = 1
high = x
ans = (low + high) / 2
num = 0
while abs(ans ** 2 - x) >= epsilon:

    num += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2

print(ans)
print(num)
