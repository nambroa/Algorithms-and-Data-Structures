from unittest import TestCase
from exercises.arrays.B_add_one_to_number.algorithm import clean_zeroes_of_number, \
    add_one_to_number


class AddOneToNumberTest(TestCase):
    def test_cleaning_zeroes_cleans_one_zero_from_the_beggining(self):
        self.assertEquals([1, 2, 3, 4], clean_zeroes_of_number([0, 1, 2, 3, 4]))

    def test_cleaning_zeroes_cleans_two_zeroes_from_the_beggining(self):
        self.assertEquals([1, 2, 3, 4], clean_zeroes_of_number([0, 0, 1, 2, 3, 4]))

    def test_cleaning_zeroes_cleans_zero_zeroes_from_the_beggining(self):
        self.assertEquals([1, 2, 3], clean_zeroes_of_number([1, 2, 3]))

    def test_add_one_to_number_adds_one_to_the_last_digit(self):
        self.assertEquals([1, 2, 3, 4, 6], add_one_to_number([1, 2, 3, 4, 5]))

    def test_add_one_to_number_adds_one_to_the_last_digit_and_cleans_two_zeroes(self):
        self.assertEquals([1, 3], add_one_to_number([0, 0, 1, 2]))

    def test_add_one_to_number_adds_one_to_the_fourth_to_last_digit_since_the_last_three_are_nine(self):
        self.assertEquals([2, 0, 0, 0], add_one_to_number([1, 9, 9, 9]))

    def test_add_one_to_number_adds_one_extra_cell_because_all_digits_were_nine(self):
        self.assertEquals([1, 0, 0], add_one_to_number([9, 9]))

