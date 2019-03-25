from unittest import TestCase

from recursion_dp_backtracking.K_permutations_with_numbers.algorithm import get_all_permutations


class PermutationsWithNumbersTest(TestCase):
    def test_permutations_of_example(self):
        expected_permutations = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        all_permutations = get_all_permutations([1, 2, 3])
        self.assertEqual(len(expected_permutations), len(all_permutations))
        for permutation in expected_permutations:
            self.assertIn(permutation, all_permutations)
