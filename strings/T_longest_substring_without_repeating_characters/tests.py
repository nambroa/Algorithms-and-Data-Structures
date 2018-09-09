from unittest import TestCase

from strings.T_longest_substring_without_repeating_characters.algorithm import \
    longest_substring_without_repeating_characters


class LongestSubstringWithoutRepeatedCharactersTest(TestCase):
    def test_length_of_longest_substring_without_repeating_characters_of_empty_string_is_0(self):
        self.assertEqual(longest_substring_without_repeating_characters(""), 0)

    def test_length_of_longest_substring_without_repeating_characters_of_abcbcaccf_is_3(self):
        self.assertEqual(longest_substring_without_repeating_characters("abcbcaccf"), 3)

    def test_length_of_longest_substring_without_repeating_characters_of_abcdbcaloccfpoiue_is_7(self):
        self.assertEqual(longest_substring_without_repeating_characters("abcdbcaloccfpoiue"), 7)