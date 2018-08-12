from unittest import TestCase

from exercises.recursion_dp_backtracking.H_generate_parenthesis.algorithm import generate_parenthesis


class GenerateParenthesisTest(TestCase):
    def test_generate_parenthesis_of_negative_amount_of_pairs_raises_exception(self):
        self.assertRaises(ValueError, generate_parenthesis, n=-6)

    def test_generate_parenthesis_of_none_raises_exception(self):
        self.assertRaises(ValueError, generate_parenthesis, n=None)

    def test_generate_parenthesis_of_0_pairs_return_empty_list(self):
        self.assertEqual(generate_parenthesis(n=0), [])

    def test_generate_parenthesis_of_1_pair_return_one_item(self):
        self.assertEqual(generate_parenthesis(n=1), ["()"])

    def test_generate_parenthesis_of_2_pairs_return_two_items(self):
        self.assertEqual(generate_parenthesis(n=2), ["(())", "()()"])

    def test_generate_parenthesis_of_3_pairs_returns_five_items(self):
        self.assertEqual(generate_parenthesis(n=3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
