from unittest import TestCase

from exercises.strings.L_longest_common_prefix.algorithm import find_longest_common_prefix_between


class LongestCommonPrefixTest(TestCase):

    def test_longest_common_prefix_should_be_abc(self):
        self.assertEqual(find_longest_common_prefix_between(['abc', 'abcde', 'abcder']), 'abc')

    def test_longest_common_prefix_should_be_an_empty_string(self):
        self.assertEqual(find_longest_common_prefix_between(['ab', 'cd']), '')

    def test_longest_common_prefix_raises_exception_on_none(self):
        self.assertRaises(ValueError, find_longest_common_prefix_between, None)

    def test_longest_common_prefix_raises_exception_on_empty_list(self):
        self.assertRaises(ValueError, find_longest_common_prefix_between, [])