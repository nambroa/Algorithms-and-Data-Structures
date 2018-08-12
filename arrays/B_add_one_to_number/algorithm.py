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
    for index in range(len(number)):
        if number[index] != 0:
            # I should cut the array here.
            number = number[index:len(number)]
            break
    return number


def add_one_to_number(number):
    if number is None or not number or len(number) == 0:
        raise ValueError("Invalid input: number is None or otherwise invalid.")
    has_been_added = False
    number = clean_zeroes_of_number(number=number)
    for index in reversed(range(len(number))):
        # Iterating over the number array in opposite order.
        digit = number[index]
        if digit != 9:
            number[index] += 1
            has_been_added = True
            break
        else:
            number[index] = 0
    if has_been_added:
        return number
    else:
        # All digits of the number are 9
        return [1] + number

