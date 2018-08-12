from unittest import TestCase

from exercises.arrays.C_max_sum_contiguous_subarray.algorithm import maximum_contiguous_subarray


class MaximumContiguousSubarrayTest(TestCase):
    def test_maximum_contiguous_subarray_returns_maximum_of_array_of_one_number(self):
        self.assertEquals(3, maximum_contiguous_subarray([3]))

    def test_maximum_contiguous_subarray_returns_maximum_of_array_of_negatives(self):
        self.assertEquals(-1, maximum_contiguous_subarray([-1, -2, -3]))

    def test_maximum_contiguous_subarray_returns_maximum_sum_of_array_of_positives_and_negatives(self):
        self.assertEquals(6, maximum_contiguous_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_maximum_contiguous_subarray_returns_maximum_sum_of_array_of_positives(self):
        self.assertEquals(10, maximum_contiguous_subarray([1, 2, 3, 4]))