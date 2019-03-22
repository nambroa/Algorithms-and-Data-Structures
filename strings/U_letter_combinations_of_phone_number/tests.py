from unittest import TestCase

from strings.U_letter_combinations_of_phone_number.algorithm import Solution


class LetterCombinationsTest(TestCase):
    def test_combinations_of_234(self):
        combinations = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg',
                        'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
        self.assertEqual(combinations, Solution().letterCombinations('234'))

    def test_combinations_of_23(self):
        combinations = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        self.assertEqual(combinations, Solution().letterCombinations('23'))

    def test_combinations_of_2(self):
        combinations = ['a', 'b', 'c']
        self.assertEqual(combinations, Solution().letterCombinations('2'))
