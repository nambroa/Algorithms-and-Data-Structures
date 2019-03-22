"""
-------------------------------------------------   LEETCODE   ---------------------------------------------------
Link to question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

2 = abc | 3 = def
4 = ghi | 5 = jkl | 6 = mno
7 = pqrs | 8 = tuv | 9 = wxyz

CLARIFYING QUESTIONS TO ASK:

+ Can the input be None? Yes
+ Can the input be an empty string? No, the string only contains digits from 2-9. Nothing more.
+ Does order matter? Is ab the same as ba? Yes, we consider them the same and you should return only one of them.

"""


# The problem says to give all possible combinations. We should start to think about recursion then.

class DigitsToLettersConverter(object):
    """

    The purpose of this object is to convert digits into the possible letter combinations.
    For example, an input of '23' would return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
    Also, an input of '2' would return ['a', 'b', 'c'].

    """

    @classmethod
    def new(cls):
        converter = cls()
        return converter

    def __init__(self):
        self._conversion_table = {'2': ['a', 'b', 'c'],
                                  '3': ['d', 'e', 'f'],
                                  '4': ['g', 'h', 'i'],
                                  '5': ['j', 'k', 'l'],
                                  '6': ['m', 'n', 'o'],
                                  '7': ['p', 'q', 'r', 's'],
                                  '8': ['t', 'u', 'v'],
                                  '9': ['w', 'x', 'y', 'z']}

    def convert_digit(self, digit):
        self._validate_digit(digit)
        return self._conversion_table[digit]

    def convert_digits(self, digits):
        letter_combinations = []
        return self._convert_digits(letter_combinations, "", digits)

    def _convert_digits(self, letter_combinations, current_combination, digits):
        if not digits:  # Base case.
            letter_combinations.append(current_combination)
            return letter_combinations
        else:
            for char in self._conversion_table[digits[0]]:
                self._convert_digits(letter_combinations, current_combination + char, digits[1:])
            return letter_combinations

    def _validate_digit(self, digit):
        if digit not in self._conversion_table.keys():
            raise ValueError("Digit must be in the 2-9 range (inclusive).")


class Solution(object):
    def letterCombinations(self, digits):
        '''
        :type digits: str
        :rtype: List[str]
        '''
        digits_to_letters_converter = DigitsToLettersConverter.new()
        if self.empty_phone(digits):
            return []
        else:
            letter_combinations = digits_to_letters_converter.convert_digits(digits)
            return letter_combinations

    def empty_phone(self, digits):
        return not digits


def _validate_phone_number(phone_number):
    if phone_number is None:
        raise ValueError("Phone number is None.")
