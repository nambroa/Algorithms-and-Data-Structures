from unittest import TestCase

from arrays.L_zero_matrix.algorithm import zero_matrix


class ZeroMatrixTest(TestCase):
    def test_zero_matrix_of_None_raises_exception(self):
        self.assertRaises(ValueError, zero_matrix, None)

    def test_zero_matrix_of_an_empty_matrix_results_in_an_empty_matrix(self):
        self.assertEqual(zero_matrix([]), [])

    def test_zero_matrix_of_2_x_2_matrix_with_one_zero_results_in_that_row_and_column_nullified(self):
        original_matrix = [[1, 2], [3, 0]]
        nullified_matrix = [[1, 0], [0, 0]]
        self.assertEqual(zero_matrix(original_matrix), nullified_matrix)

    def test_zero_matrix_of_4_x_3_matrix_with_first_row_full_of_zeroes_nullifies_the_entire_matrix(self):
        original_matrix = [[0, 0, 0, 0], [1, 2, 3, 4], [5, 6, 7, 8]]
        nullified_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(zero_matrix(original_matrix), nullified_matrix)
