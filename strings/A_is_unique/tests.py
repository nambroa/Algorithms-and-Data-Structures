from unittest import TestCase

from strings.A_is_unique.algorithm import check_if_word_has_all_unique_characters


class IsUniqueTest(TestCase):
    def test_a_word_with_repeated_chars_should_not_be_unique(self):
        self.assertFalse(check_if_word_has_all_unique_characters('aab'))

    def test_a_word_with_no_repeated_chars_should_be_unique(self):
        self.assertTrue(check_if_word_has_all_unique_characters('abc'))

    def test_an_empty_word_should_be_unique(self):
        self.assertTrue(check_if_word_has_all_unique_characters(''))

    def test_checking_uniqueness_of_none_should_raise_exception(self):
        self.assertRaises(ValueError, check_if_word_has_all_unique_characters, None)
