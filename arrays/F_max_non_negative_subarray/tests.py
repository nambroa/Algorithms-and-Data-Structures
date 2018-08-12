from unittest import TestCase

from exercises.arrays.F_max_non_negative_subarray.algorithm import maximum_non_negative_subarray


class MaximumNonNegativeSubarrayTest(TestCase):
    def test_maximum_non_negative_subarray_returns_a_subarray_with_only_one_element(self):
        self.assertEquals([424238335], maximum_non_negative_subarray([-846930886, -1714636915, 424238335, -1649760492]))

    def test_maximum_non_negative_subarray_returns_best_subarray_out_of_two_possible_ones(self):
        self.assertEquals([1, 2, 5], maximum_non_negative_subarray([1, 2, 5, -7, 2, 3]))