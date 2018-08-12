from unittest import TestCase

from strings.E_one_away.algorithm import one_away


class OneAwayTest(TestCase):
    def test_one_away_should_properly_detect_when_strings_are_one_edit_away(self):
        self.assertTrue(one_away('abc', 'abcd'))

    def test_one_away_should_properly_detect_when_strings_are_not_one_edit_away(self):
        self.assertFalse(one_away('a', 'abcderg'))

    def test_an_empty_string_is_only_one_edit_away_from_one_char_strings(self):
        self.assertTrue(one_away('', 'a'))

    def test_an_empty_string_is_not_one_edit_away_from_two_char_strings(self):
        self.assertFalse(one_away('', 'ab'))