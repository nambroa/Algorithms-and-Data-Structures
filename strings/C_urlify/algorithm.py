"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 3
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters.
You may assume that you are given the "true" length of the string.
(non-extended ASCII string, 128 possible chars) --> ASK THIS IN INTERVIEW.

QUESTIONS:

+ Can the string be None, empty, or invalid struct like int? No. You may assume input is 100% sanitized.

"""


def is_space(letter):
    return letter == ' '


def urlify(string1):
    # Function is so simple I don't think I need tests for now. Will add them later when I have the extra time!
    return string1.replace(' ', '%20')
