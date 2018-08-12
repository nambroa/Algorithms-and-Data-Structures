"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 1
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures? (non-extended ASCII string, 128 possible chars)

QUESTIONS:

+ Can the input be an empty string? If so, what should I return? Yes, return True
+ Can the input be None? Yes. Is it okay to raise an exception? Yes.
+ Can the input be invalid? Like an integer? No

"""

"""

Simple. Make a set of appearances, when you get higher than 1 appearance, break. Otherwise, return True.

Complexity: O(n)

"""


def check_if_word_has_all_unique_characters(word):
    if word is None:
        raise ValueError("Word is None.")
    unique_appearances = set()
    for letter in word:
        if letter in unique_appearances:
            return False
        unique_appearances.add(letter)
    return True


"""

Follow-up: What if you cannot use additional data structures?
For example, for your previous algorithm, you cannot use a set.
It's much less efficient, but you could check if the first letter of the string appears in the rest by just iterating
over it. You do that for every letter, and you can check for uniqueness in O(n^2).

I'm not going to code that because:
"""


def aint_nobody_got_time_fo_dat():
    return True
