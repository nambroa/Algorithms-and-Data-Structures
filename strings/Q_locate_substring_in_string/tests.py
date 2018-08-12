from unittest import TestCase

from strings.Q_locate_substring_in_string.algorithm import locate_substring_in_string


class LocateSubstringInStringTest(TestCase):

    def test_locate_substring_in_large_string_returns_its_starting_index(self):
        string = 'aaaaabbabbaaaababbbbaaabbbaababaababbaabaabaaabbabab'
        substring = 'bbbaababaa'
        self.assertEqual(locate_substring_in_string(substring, string), 23)

    def test_locate_substring_in_large_string_returns_minus_one_when_it_is_not_present(self):
        string = 'aaaaabbabbaaaababbbbaaabbbaababaababbaabaabaaabbabab'
        substring = 'bbbaabaaabaa'
        self.assertEqual(locate_substring_in_string(substring, string), -1)

    def test_locate_substring_in_large_string_returns_minus_one_if_the_string_is_empty(self):
        string = ''
        substring = 'bbbaababaa'
        self.assertEqual(locate_substring_in_string(substring, string), -1)

    def test_locate_substring_in_large_string_returns_minus_one_if_the_substring_is_empty(self):
        string = 'aaaaabbabbaaaababbbbaaabbbaababaababbaabaabaaabbabab'
        substring = ''
        self.assertEqual(locate_substring_in_string(substring, string), -1)