# def custom_is_decimal(string: str) -> bool:
#     try:
#         for s in string:
#             if type(int(s)) != int:
#                 return False
#         return True
#     except ValueError:
#         return False


# x = custom_is_decimal('sss1')
# print(x)

def custom_in_keyword(s, string):
    for s in string:
        if 'a' == s:
            return True
    return False


print(custom_in_keyword('a', 'safgh'))
