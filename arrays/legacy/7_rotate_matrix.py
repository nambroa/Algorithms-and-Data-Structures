"""

ARRAY AND STRINGS - QUESTION 7
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes.
Write a method to rotate the image by 90 degrees. Do it in place (no extra memory allowed).
Matrix comes as an array of arrays. Example: [[row_1], [row_2], .., [row_n]] --> ASK THIS IN INTERVIEW

"""


def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        # Matrix is empty or is not squared.
        return False
    n = len(matrix)
    for layer in range(n/2):
        # The layers determine the range of your transformation
        # For example on layer 0 you will only swap the outer edge of the matrix.
        # A matrix of NxN has N/2 layers.
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top.
            top = matrix[first][i]
            # Left -> Top rotation
            matrix[first][i] = matrix[last-offset][first]
            # Bottom -> Left rotation
            matrix[last-offset][first] = matrix[last][last-offset]
            # Right -> Bottom rotation
            matrix[last][last-offset] = matrix[i][last]
            # Top -> Right rotation
            matrix[i][last] = top
    return matrix


assert rotate_matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
rotated_matrix2 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
assert rotate_matrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == rotated_matrix2
assert not rotate_matrix([[1], [2], [3]])
assert not rotate_matrix([])