from unittest import TestCase

from strings.B_check_permutation.algorithm import check_permutation_between


class CheckPermutationTest(TestCase):
    def test_two_permutable_strings_should_be_permutations(self):
        self.assertTrue(check_permutation_between('abcd', 'dacb'))

    def test_two_non_permutable_strings_should_not_be_permutations(self):
        self.assertFalse(check_permutation_between('abcd', 'boiuty'))
