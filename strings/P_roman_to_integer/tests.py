from unittest import TestCase

from strings.P_roman_to_integer.algorithm import convert_roman_to_integer


class RomanToIntegerTest(TestCase):

    def test_converting_none_to_integer_raises_exception(self):
        self.assertRaises(ValueError, convert_roman_to_integer, None)

    def test_converting_empty_roman_to_integer_returns_zero(self):
        self.assertEqual(convert_roman_to_integer(''), 0)

    def test_converting_four_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('IV'), 4)

    def test_converting_nine_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('IX'), 9)

    def test_converting_ten_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('X'), 10)

    def test_converting_thirteen_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('XIII'), 13)

    def test_converting_forty_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('XL'), 40)

    def test_converting_forty_nine_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('XLIX'), 49)

    def test_converting_ninety_in_roman_to_integer(self):
        self.assertEqual(convert_roman_to_integer('XC'), 90)

