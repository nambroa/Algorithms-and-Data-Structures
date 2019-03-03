from unittest import TestCase
from arrays.K_rotate_matrix.algorithm import rotate_matrix


class RotateMatrixTest(TestCase):
    def test_rotate_matrix_of_3_by_3(self):
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], rotate_matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_rotate_matrix_of_4_by_4(self):
        rotated_matrix = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(rotated_matrix,
                         rotate_matrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

    def test_rotate_empty_matrix_raises_exception(self):
        self.assertRaises(ValueError, rotate_matrix, [])

    def test_rotate_not_squared_matrix_raises_exception(self):
        self.assertRaises(ValueError, rotate_matrix, [[1], [2], [3]])
