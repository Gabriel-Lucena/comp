size = int(input())


def string_to_list_int(string_input):
    vector_strings = string_input.split()
    int_list = []

    for i_list_input in vector_strings:
        int_list.append(int(i_list_input))

    return int_list


matrix = []

for i in range(size):

    user_input = input()

    matrix.append(string_to_list_int(user_input))


def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


def verify_horizontal_sum(matrix, size):
    sum_vector = []
    soma_int = 0

    for column in range(size):

        for row in range(size):

            soma_int += matrix[column][row]

        sum_vector.append(soma_int)

        soma_int = 0

    return all_equal(sum_vector)


def verify_vertical_sum(matriz, size):
    sum_vector = []
    sum_int = 0

    for i in range(size):

        for column in range(size):

            sum_int += matriz[i][column]

        sum_vector.append(sum_int)

        sum_int = 0

    return all_equal(sum_vector)


def verify_diagonal_sum(matriz, size):
    sum_vector = []
    sum_int = 0

    for i in range(size):

        sum_int += matriz[i][i]

    sum_vector.append(sum_int)

    sum_int = 0

    for i in range(size):

        for column in range(0, size):

            sum_int += matriz[i][column]

        sum_vector.append(sum_int)

        sum_int = 0

    return all_equal(sum_vector)


def verify_matrix(matrix, size):

    sum = 0

    for i in range(size):
        sum += matrix[0][i]

    if verify_horizontal_sum(matrix, size) and verify_vertical_sum(matrix, size) and  \
            verify_diagonal_sum(matrix, size):
        return sum
    else:
        return -1


print(verify_matrix(matrix, size))
