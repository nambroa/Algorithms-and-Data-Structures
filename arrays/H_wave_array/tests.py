from unittest import TestCase

from exercises.arrays.H_wave_array.algorithm import create_wave_list_from


class WaveArrayTest(TestCase):
    def test_wave_array_raises_exception_if_none_is_found(self):
        self.assertRaises(ValueError, create_wave_list_from, None)

    def test_wave_array_raises_exception_if_no_numbers_are_found(self):
        self.assertRaises(ValueError, create_wave_list_from, [])

    def test_wave_array_function_returns_the_lexicographically_smallest_wave_array(self):
        self.assertEquals([2, 1, 4, 3], create_wave_list_from([1, 4, 3, 2]))

    def test_wave_array_function_returns_the_correct_wave_array_from_list(self):
        self.assertEquals([2, 1, 5, 4, 9, 7, 17, 11, 99], create_wave_list_from([1, 7, 4, 9, 11, 2, 17, 99, 5]))
