# a = input("> ")


def custom_reverse(a):  # a= 'ab' last = 'b' other = 'a'

    if len(a) == 1:
        return a
    last = a[-1]
    other = a[:-1]
    return last + custom_reverse(other)  # c + b + a


x = custom_reverse('abc')
print(x)

# def custom_reverse(a):
#     string_list = list(a)
#     string_list.reverse()

#     string = ''.join(string_list)

# string = ''
# for item in string_list:
#     string += item
#     return string


# x = custom_reverse('abc')
# print(x)
