from unittest import TestCase

from exercises.strings.N_length_of_last_word.algorithm import get_length_of_last_word

# NOTE: Unittests should only test one case at a time. I aggregate them here just for comfort.


class LengthOfLastWordTest(TestCase):
    def test_length_of_last_word_of_empty_string_and_only_spaces_should_be_zero(self):
        self.assertEqual(get_length_of_last_word("       "), 0)
        self.assertEqual(get_length_of_last_word(""), 0)

    def test_length_of_last_word_several_cases(self):
        self.assertEqual(get_length_of_last_word("hola como estas queeeeee    "), 8)
        self.assertEqual(get_length_of_last_word("hola"), 4)
        self.assertEqual(get_length_of_last_word("opk oer"), 3)

