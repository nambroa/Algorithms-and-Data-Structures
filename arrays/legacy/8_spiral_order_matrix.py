"""

Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order

For example, given n = 3, the matrix should look like this:

1 2 3
8 9 4
7 6 5

Questions to ask:
Can n be negative? NO
Will n always be an integer positive number? YES
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers

    def generateMatrix(self, A):
        matrix = [[0] * A for count in xrange(A)]
        left = top = 0
        right = bottom = A - 1
        direction = 0
        count = 1
        while left <= right and top <= bottom:
            # Moving from left to right
            if direction == 0:
                for i in xrange(left, right + 1):
                    matrix[top][i] = count
                    count += 1
                direction = 1
                top += 1
            # Moving from top to bottom
            elif direction == 1:
                for i in xrange(top, bottom + 1):
                    matrix[i][right] = count
                    count += 1
                direction = 2
                right -= 1
            # Moving from right to left
            elif direction == 2:
                for i in xrange(right, left - 1, -1):
                    matrix[bottom][i] = count
                    count += 1
                direction = 3
                bottom -= 1
            else:
                # Moving from top to bottom
                for i in xrange(bottom, top - 1, -1):
                    matrix[i][left] = count
                    count += 1
                direction = 0
                left += 1
        return matrix

