"""

ARRAY AND STRINGS - QUESTION 7
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes.
Write a method to rotate the image by 90 degrees. Do it in place (no extra memory allowed).
Matrix comes as an array of arrays. Example: [[row_1], [row_2], .., [row_n]] --> ASK THIS IN INTERVIEW

"""

"""

The main idea of the algorithm is to note that each row of the original matrix will impact each row on the
rotated matrix in a similar manner. This is the core principle:

+ The first row of the rotated matrix will be the first row the original one, but with the elements filled
 in opposite orderFirst row of source –> First column of destination, elements filled in opposite order.

And this repeats for each row.

Since we have to do this in place, we will replace the items by layers. Otherwise, we would be overriding places
in the matrix we already changed. Think of the matrix as an onion. A matrix of 3x3 has an outer layer, an inner layer
and 1 number in the center. Thus, a NxN matrix has N/2 layers.

"""


def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is empty or is not squared.")
    n = len(matrix)
    for layer in range(int(n/2)):
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


