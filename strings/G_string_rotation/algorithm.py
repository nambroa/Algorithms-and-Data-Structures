"""

---------------------------------- Cracking the Coding Interview ----------------------------------

ARRAY AND STRINGS - QUESTION 9

Assume you have a method isSubString which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one to isSubString.
Example: "waterbottle" is a rotation of "erbottlewat"
         "waterbottle" is NOT a rotation of "teawbortlt" --> Structure must be preserved!

QUESTIONS:

+ Can you provide examples? Yes (see above).
+ Can the input be None or the string be empty? Yes to both.
+ Is the string limited to a set of characters? For example only lowercase, only uppercase, etc? Only lowercase a-z.
+ Can the string have spaces? No

"""


"""

At first, you should check if s1 and s2 differ in length. If they do, they will never be a rotation of each other.

Afterwards, the idea is to store string1 duplicated. For example, s1='waterbottlewaterbottle'. That is because
when you store it duplicated, you also store all possible rotations of it. Then you can use s2 in s1 to check for
rotation, super simple.

O(2*|s1|)

"""


def is_substring(string1, string2):
    return string2 in string1


def is_rotation(string1, string2):
    if string1 is None or string2 is None: raise ValueError("Some of the strings are None.")
    if len(string2) == 0: return len(string1) == 0
    if len(string1) != len(string2): return False
    string1 += string1
    if is_substring(string1, string2):
        return True
    return False

