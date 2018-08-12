"""

String T always consists of two distinct alternating characters.
For example, if string T's two distinct characters are x and y, then t could be xyxyx or yxyxy but not xxyy or xyyx.

You can convert some string S to string T by deleting characters from S.
When you delete a character from S, you must delete all occurrences of it in S.
For example, if  S=abaacdabd and you delete the character a, then the string becomes bcdbd.

Given S, convert it to the longest possible string T made up only of alternating characters.
Then print the length of string T on a new line; if no string T can be formed from S, print 0 instead.

Example input: beabeefeab
The characters present in  are a, b, e, and f. This means that T must consist of two of those characters and we must
delete two others. Our choices for characters to leave are [a,b], [a,e], [a, f], [b, e], [b, f] and [e, f].
If we delete e and f, the resulting string is babab. This is a valid  as there are only two distinct characters
(a and b), and they are alternating within the string.
If we delete a and f, the resulting string is bebeeeb. This is not a valid string because there are consecutive
e's present. Removing them would leave consecutive b's, so this fails to produce a valid string .
Other cases are solved similarly.
babab is the longest string we can create.
Example output: 5 (the length of string T)

"""
import itertools

"""

The idea goes as follows:

A) Get all pairs of chars present in the string.
B) Remove all chars in the string except for those of pair i.
C) See if it's a valid string
C1) If it is, then check if it's of max length.
C2) If it isn't, move to the next pair
D) Return the T of maxmimum length. If no T was found, return 0.

"""


def is_a_valid_t_string(string):
    if len(string) < 2:
        return False
    first_char = string[0]
    second_char = string[1]
    if first_char != second_char:
        for i in range(2, len(string)):
            ith_char = string[i]
            if i % 2 == 0 and ith_char != first_char:
                return False
            elif i % 2 == 1 and ith_char != second_char:
                return False
    else:
        return False
    return True


# This function removes all chars from the string that are not first_char or second_char
def _remove_all_chars_from_string_except(first_char, second_char, string):
    new_string = string.replace(first_char, '')
    new_string = new_string.replace(second_char, '')
    return new_string


def two_characters(string):
    pairwise_permutations = itertools.combinations(string, 2)
    max_length_of_t_string = 0
    for pairwise_permutation in pairwise_permutations:
        first_char = pairwise_permutation[0]
        second_char = pairwise_permutation[1]
        curated_string = _remove_all_chars_from_string_except(first_char, second_char, string)
        if is_a_valid_t_string(curated_string):
            # check length
            max_length_of_t_string = max(max_length_of_t_string, len(curated_string))
    return max_length_of_t_string