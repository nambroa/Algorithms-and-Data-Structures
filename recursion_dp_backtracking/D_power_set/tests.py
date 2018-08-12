from unittest import TestCase

from exercises.recursion_dp_backtracking.D_power_set.algorithm import get_all_subsets_of


class PowerSetTest(TestCase):
    def test_power_set_of_empty_set_is_empty_set(self):
        answer = [[]]
        self.assertEqual(get_all_subsets_of(set()), answer)

    def test_power_set_of_set_of_two_should_be_3_sets(self):
        answer = [[0, 1], [1], [0], []]
        self.assertListEqual(get_all_subsets_of([0, 1]), answer)

    def test_power_set_of_set_of_three_should_be_8_sets(self):
        answer = [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]
        self.assertListEqual(get_all_subsets_of([1, 2, 3]), answer)
