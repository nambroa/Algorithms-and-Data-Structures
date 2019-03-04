"""

ARRAY AND STRINGS - QUESTION 8
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
Matrix comes as an array of arrays. Example: [[row_1], [row_2], .., [row_n]] --> ASK THIS IN INTERVIEW

"""


def _check_if_matrix_is_none(matrix):
    if matrix is None:
        raise ValueError("Matrix is None.")


def _nullify(matrix, row, column):
    # Nullify puts 0's in the specified column and row of the matrix given as input.
    if row is not None:
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
    else:
        for i in range(len(matrix)):
            matrix[i][column] = 0


def _check_if_the_first_row_and_column_have_zeroes(matrix):
    first_row_has_zeroes = False
    first_col_has_zeroes = False

    # Since I'm going to be using the first row and column to store relevant information from other rows and columns,
    # I need the original data found in those positions stored somewhere else that does not affect space complexity.

    # Check if first row has zeroes
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            first_row_has_zeroes = True
            break

    # Check if first column has zeroes
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zeroes = True
            break
    return first_col_has_zeroes, first_row_has_zeroes


# This algorithm uses the first row and first column of the matrix to store relevant information.
# This makes the space complexity O(1).
def zero_matrix(matrix):
    _check_if_matrix_is_none(matrix)
    if len(matrix) == 0:
        return matrix
    first_col_has_zeroes, first_row_has_zeroes = _check_if_the_first_row_and_column_have_zeroes(matrix)

    # After saving the info from the first row and column, I can check for zeroes all through the matrix and store
    # their positions in the first row and column of the matrix. So, if A[i][j] == 0, I know the row i and column j
    # will need to be filled with 0's. Then, I can store a 0 in the first row, position j, to know that the column j
    # needs 0's. Likewise, I can store a 0 in the first column, position i, to know that the row i needs 0's.

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == 0:
                matrix[0][col_index] = 0
                matrix[row_index][0] = 0

    # After storing all the relevant information, I iterate the first row and column, nullifying the matrix as needed.

    # Check for zeroes on first row, and nullify those columns.
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            _nullify(matrix=matrix, column=i, row=None)

    # Check for zeroes on first column, and nullify those rows.
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            _nullify(matrix=matrix, column=None, row=i)

    # Lastly, if I found a 0 in the first column or row, I nullify those positions.

    if first_col_has_zeroes:
        _nullify(matrix=matrix, column=0, row=None)

    if first_row_has_zeroes:
        _nullify(matrix=matrix, column=None, row=0)
    return matrix
