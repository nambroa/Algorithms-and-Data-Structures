"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 4
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
(alphabet string CAN HAVE SPACES, lower and uppercase NEED to be treated as equals) --> ASK THIS IN INTERVIEW.

-----------EXAMPLE BEGIN-----------
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc)
-----------EXAMPLE END-----------

QUESTIONS:

+ Can the string be None or empty? Yes
+ Should I treat uppercase and lowercase letters differently or as equals? As equals
+ Can the string have spaces? Yes. Should I take them into account? Yes.

"""

# A more intuitive way to look at it: return s == s[::-1]
import itertools


def palindrome(s):
    return s[len(s) / 2:] == s[(len(s) - 1) / 2:: -1]


def simple_way_to_get_all_permutations_of(string):
    return list(itertools.permutations(string))


# A permutation of a palindrome can have at most one char with an odd number of apparitions.
# Since I need to treat lowercase and uppercase equally, I convert all to lowercase.
def is_permutation_of_palindrome(string):
    if string is None: raise ValueError("String is None.")
    if len(string) == 0 or len(string) == 1: return True
    char_appearances = {}
    string = string.lower()
    for char in string:
        try:
            char_appearances[char] += 1
        except KeyError:
            char_appearances[char] = 1
    found = False
    for char, number_of_appearances in char_appearances.items():
        if number_of_appearances % 2 == 1:
            if found:
                return False
            else:
                found = True
    return True
