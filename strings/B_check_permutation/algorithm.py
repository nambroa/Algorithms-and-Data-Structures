"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 2
Given two strings, write a method to decide if one is a permutation of the other.
(non-extended ASCII string, 128 possible chars) --> ASK THIS IN INTERVIEW.


QUESTIONS:

+ Can any of the strings come as None or invalid, like int? It can come as None or a proper string.
+ Can one or both strings be empty? Yes

"""

"""

To be a permutation, you need to have the same letters in the same or different order. So we are going to build a
dictionary of chars from string1, and then subtract from the same dict each time we find the char in string2.
At the end, if they are a permutation of each other, the dict should be empty.

"""


def check_permutation_between(string1, string2):
    if string1 is None or string2 is None:
        raise ValueError("String is None")
    char_appearances = {}
    for char in string1:
        try:
            char_appearances[char] += 1
        except KeyError:
            char_appearances[char] = 1
    for char in string2:
        try:
            char_appearances[char] -= 1
            if char_appearances[char] == 0:
                char_appearances.pop(char, None)
        except KeyError:
            return False
    return not bool(char_appearances)


