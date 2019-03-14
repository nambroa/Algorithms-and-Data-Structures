from unittest import TestCase

from strings.I_camelcase.algorithm import amount_of_words_in_camelcase


class NumberOfWordsTest(TestCase):

    def test_returns_1_word_for_string_a(self):
        string = "a"
        self.assertEqual(amount_of_words_in_camelcase(string), 1)

    def test_returns_2_words_for_string_hiCat(self):
        string = "hiCat"
        self.assertEqual(amount_of_words_in_camelcase(string), 2)

    def test_returns_6_words_for_string(self):
        string = "hiCatHow Are You Doing"
        self.assertEqual(amount_of_words_in_camelcase(string), 6)
