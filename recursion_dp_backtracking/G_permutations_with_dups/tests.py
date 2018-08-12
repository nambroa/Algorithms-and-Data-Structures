from unittest import TestCase

from recursion_dp_backtracking.G_permutations_with_dups.algorithm import get_all_non_repeated_permutations_of, \
    better_get_all_non_repeated_permutations_of


class PermutationsWithDupsTest(TestCase):
    def test_permutations_of_empty_string_are_just_empty_string(self):
        self.assertEqual(get_all_non_repeated_permutations_of(""), [""])

    def test_permutations_of_char_are_just_that_char(self):
        self.assertEqual(get_all_non_repeated_permutations_of("a"), ["a"])

    def test_there_are_2_permutations_for_a_2_char_string(self):
        permutations = ["ab", "ba"]
        self.assertListEqual(get_all_non_repeated_permutations_of("ab"), permutations)

    def test_there_are_6_permutations_for_a_3_char_string(self):
        permutations = ["abc", "bac", "bca", "acb", "cab", "cba"]
        self.assertListEqual(get_all_non_repeated_permutations_of("abc"), permutations)

    def test_there_are_3_permutations_for_a_3_char_string_with_duplicates(self):
        permutations = ["aba", "baa", "aab"]
        self.assertListEqual(get_all_non_repeated_permutations_of("aba"), permutations)

    def test_there_are_1_permutations_for_a_1_char_string_full_of_duplicates(self):
        self.assertListEqual(get_all_non_repeated_permutations_of("aaaaaaaaaa"), ["aaaaaaaaaa"])


class BetterPermutationsWithDupsTest(TestCase):
    def test_permutations_of_empty_string_are_just_empty_string(self):
        self.assertEqual(better_get_all_non_repeated_permutations_of(""), [""])

    def test_permutations_of_char_are_just_that_char(self):
        self.assertEqual(better_get_all_non_repeated_permutations_of("a"), ["a"])

    def test_there_are_2_permutations_for_a_2_char_string(self):
        permutations = ["ab", "ba"]
        self.assertListEqual(better_get_all_non_repeated_permutations_of("ab"), permutations)

    def test_there_are_6_permutations_for_a_3_char_string(self):
        permutations = ["abc", "acb", "bac", "bca", "cab", "cba"]
        self.assertListEqual(better_get_all_non_repeated_permutations_of("abc"), permutations)

    def test_there_are_3_permutations_for_a_3_char_string_with_duplicates(self):
        permutations = ["aab", "aba", "baa"]
        self.assertListEqual(better_get_all_non_repeated_permutations_of("aba"), permutations)

    def test_there_are_1_permutations_for_a_1_char_string_full_of_duplicates(self):
        self.assertListEqual(better_get_all_non_repeated_permutations_of("aaaaaaaaaa"), ["aaaaaaaaaa"])

