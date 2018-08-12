from unittest import TestCase

from recursion_dp_backtracking.F_permutations_without_dups.algorithm import get_all_permutations_of


class PermutationsWithoutDupsTest(TestCase):
    def test_trying_to_obtain_permutations_of_none_should_raise_exception(self):
        self.assertRaises(ValueError, get_all_permutations_of, None)

    def test_the_number_of_permutations_of_empty_string_should_be_empty_string(self):
        permutations = ''
        self.assertEqual(get_all_permutations_of(''), permutations)

    def test_the_number_of_permutations_of_a_should_be_one(self):
        permutations = ['a']
        self.assertListEqual(get_all_permutations_of('a'), permutations)

    def test_the_number_of_permutations_of_ab_should_be_two(self):
        permutations = ['ab', 'ba']
        self.assertListEqual(get_all_permutations_of('ab'), permutations)

    def test_the_number_of_permutations_of_abc_should_be_six(self):
        permutations = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        self.assertListEqual(get_all_permutations_of('abc'), permutations)