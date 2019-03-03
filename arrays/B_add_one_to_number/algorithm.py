# coding=utf-8
"""

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

EXAMPLE:

If the vector has [1, 2, 3], the returned vector should be [1, 2, 4], as 123 + 1 = 124.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

"""
# Question: Can the input contain invalid data? Structs, strings... Answer: NO. Input is always valid.
# Question: Can the input be None: Answer: YES. You should check it.

# IDEA: Algorithm steps are as follows:
# PRE: Check if input is None.
# A: Clean zeroes from the left from the input.
# B: Add 1 to the last digit. If the digit is 9, change it to zero and add 1 to the previous one
#    EDGE CASE: If all numbers are 9, add one space at the beginning and put a 1 there, all other digits to 0.


def clean_zeroes_of_number(number):
    for index, digit in enumerate(number):
        if digit != 0:
            return number[index:]
    return number  # If all digits are zeroes


def check_if_number_is_none(number):
    if number is None:
        raise ValueError("Number is None.")


def check_if_number_is_empty(number):
    if len(number) is None:
        raise ValueError("Number is empty.")


def add_one_to_number(number):
    check_if_number_is_none(number)
    check_if_number_is_empty(number)
    new_number = clean_zeroes_of_number(number)
    current_index = len(new_number) - 1
    for digit in new_number[::-1]:
        if digit != 9:
            return new_number[:current_index] + [digit+1] + new_number[current_index+1:]
        else:
            new_number[current_index] = 0
        current_index -= 1
    return [1] + new_number
