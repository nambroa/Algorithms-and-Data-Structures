from unittest import TestCase

from exercises.arrays.E_repeat_and_missing_number.algorithm import \
    get_repeated_and_missing_number


class RepeatAndMissingNumberTest(TestCase):
    def test_missing_number_and_repeat_throws_exception_when_no_list_is_given(self):
        self.assertRaises(ValueError, get_repeated_and_missing_number, None)

    def test_missing_number_and_repeat_throws_exception_when_empty_list_is_given(self):
        self.assertRaises(ValueError, get_repeated_and_missing_number, [])

    def test_missing_number_and_repeat_are_found_successfully(self):
        self.assertEquals((1, 3), get_repeated_and_missing_number([1, 1, 2, 4, 5]))

    def test_missing_number_and_repeat_are_found_when_the_missing_one_was_the_last_one_in_the_array(self):
        self.assertEquals((2, 5), get_repeated_and_missing_number([1, 2, 2, 3, 4]))

    def test_stress_test_for_missing_number_and_repeat(self):
        self.assertEquals((7, 11), get_repeated_and_missing_number([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17]))
