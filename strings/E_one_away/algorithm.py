"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 5
There are three types of edits that can be performed on strings: insert, remove or replace a character.
Given two strings, write a function to check if there are one edit (or zero edits) away.
(non-extended ASCII string, 128 possible chars) --> ASK THIS IN INTERVIEW.

-----------EXAMPLE BEGIN-----------
pale, ple --> True
pale, pales --> True
pale, bale --> True
pale, bake --> False
-----------EXAMPLE END-----------

QUESTIONS

+ Can you provide examples? Yes, (see above)
+ Can the input be invalid or None? It can be None
+ Can the strings be empty? Yes, treat is as usual. (empty is one edit away from the one-char-string only)

"""

"""

The type of edit away doesn't matter really. It only matters if it's different on that char space.
The complexity of this function is O(min(|s1|, |s2|)).

"""


def one_away(s1, s2):
    if s1 is None or s2 is None:
        raise ValueError("Input is partially/completely None.")
    # If the length difference between the strings is greater than 1, then they are more than 1 edit away.
    edits_away = abs(len(s1) - len(s2))
    if edits_away > 1:
        return False
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            edits_away += 1
            if edits_away > 1:
                return False
    return edits_away <= 1
