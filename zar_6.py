# input : "1000100011002200"
# output : ['1', '000', '1', '000', '11', '00', '22', '00']

# word_digits = "1000100011002200"
# output = []
# count = 0
# start = 0
# for i in range(len(word_digits)-1):  # i = 5     count = 6    start = 6
#     if word_digits[i] == word_digits[i+1]:
#         count += 1
#     else:
#         output.append(word_digits[start:count+1])
#         start = count + 1
#         count += 1
# else:
#     output.append(word_digits[start:count+1])


# print(output)


############################################

# how to define function inside another function:


def isPalindromic(string):
    def tochars(string):
        string = string.lower()
        characters = ''
        for char in string:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                characters += char
        return characters

    def isPal(string):
        if len(string) <= 1:
            return True
        elif string[0] == string[-1] and isPal(string[1:-1]):
            return True
        else:
            return False
    return isPal(tochars(string))


x = "aabbaa"
out = isPalindromic(x)
if out:

    print(f'{x} is Palindromic')
else:
    print(f'{x} is Not Palindromic')


# exercise: write above code three time and analys it
# exercise : write a function to calculates n! > with recursive function and without recursive
azar_3
