matrix = [[1, 2, 12, 46], [30, 14, 32, 78], [25, 14, 19, 2]]
# print(matrix)
# print(matrix[0][0])

# define a function to find max value in matrix


def max_value(matrix):
    pass


# print(matrix)


def printmx(matrix):
    for row in matrix:
        for cel in row:
            print(f'{cel:4d}', end='')

        print()


printmx(matrix)


def size(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return (rows, columns)


print(size(matrix))


def transpose(matrix):
    pass
