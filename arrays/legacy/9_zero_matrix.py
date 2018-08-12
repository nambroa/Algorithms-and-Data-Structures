"""

ARRAY AND STRINGS - QUESTION 8
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
Matrix comes as an array of arrays. Example: [[row_1], [row_2], .., [row_n]] --> ASK THIS IN INTERVIEW

"""


def nullify(matrix, row, column):
    if row is not None:
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
    else:
        for i in range(len(matrix)):
            matrix[i][column] = 0


# This algorithm uses the first row and first column of the matrix to store relevant space.
# This makes the space big O = O(1).
def zero_matrix(matrix):
    if not matrix:
        # Empty matrix
        return matrix
    first_row_has_zeroes = False
    first_col_has_zeroes = False

    # Check if first row has zeroes
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            first_row_has_zeroes = True

    # Check if first column has zeroes
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zeroes = True

    # Check for zeroes in the matrix and store their relevant positions in the first row/column of the matrix.
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == 0:
                matrix[0][col_index] = 0
                matrix[row_index][0] = 0

    # Nullify the matrix! Check for zeroes on first row, and nullify those columns.
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            nullify(matrix=matrix, column=i, row=None)

    # Nullify the matrix! Check for zeroes on first column, and nullify those rows.
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullify(matrix=matrix, column=None, row=i)

    if first_col_has_zeroes:
        nullify(matrix=matrix, column=0, row=None)

    if first_row_has_zeroes:
        nullify(matrix=matrix, column=None, row=0)
    return matrix


assert zero_matrix([]) == []
assert zero_matrix([[1, 2], [3, 0]]) == [[1, 0], [0, 0]]
assert zero_matrix([[0, 0, 0, 0], [1, 2, 3, 4], [5, 6, 7, 8]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]