# coding=utf-8

from unittest import TestCase

from strings.S_longest_palindromic_substring.algorithm import longest_palindromic_substring


class LongestPalindromicSubstringTest(TestCase):
    def test_longest_palindromic_substring_of_kcabba_is_abba(self):
        self.assertEqual(longest_palindromic_substring("kcabba"), "abba")

    def test_longest_palindromic_substring_of_rekcabbamuyopllpo_is_opllpo(self):
        self.assertEqual(longest_palindromic_substring("rekcabbamuyopllpo"), "opllpo")

    def test_longest_palindromic_substring_of_rekcabbamuyopllporehdpoiuyttyuiopmty_is_poiuyttyuiop(self):
        self.assertEqual(longest_palindromic_substring("rekcabbamuyopllporehdpoiuyttyuiopmty"), "poiuyttyuiop")
