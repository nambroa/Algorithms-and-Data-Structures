from unittest import TestCase

from exercises.recursion_dp_backtracking.E_recursive_multiply.algorithm import iterative_multiply, recursive_multiply


class IterativeMultiplyTest(TestCase):
    def test_multiplying_one_and_one_returns_one_as_the_answer(self):
        self.assertEqual(iterative_multiply(1, 1), 1)

    def test_multiplying_one_and_zero_returns_zero_as_the_answer(self):
        self.assertEqual(iterative_multiply(1, 0), 0)

    def test_multiplying_two_and_two_returns_four_as_the_answer(self):
        self.assertEqual(iterative_multiply(2, 2), 4)

    def test_multiplying_four_and_six_returns_twenty_four_as_the_answer(self):
        self.assertEqual(iterative_multiply(4, 6), 24)


class RecursiveMultiplyTest(TestCase):
    def test_multiplying_one_and_one_returns_one_as_the_answer(self):
        self.assertEqual(recursive_multiply(1, 1), 1)

    def test_multiplying_one_and_zero_returns_zero_as_the_answer(self):
        self.assertEqual(recursive_multiply(1, 0), 0)

    def test_multiplying_two_and_two_returns_four_as_the_answer(self):
        self.assertEqual(recursive_multiply(2, 2), 4)

    def test_multiplying_four_and_six_returns_twenty_four_as_the_answer(self):
        self.assertEqual(recursive_multiply(4, 6), 24)