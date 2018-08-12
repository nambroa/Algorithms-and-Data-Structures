"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the
length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

QUESTIONS:

+ Can the input be None? Yes
+ Can the input be ''? Yes
+ Can the input be just empty spaces? Like '            '? Yes

"""


def get_length_of_last_word(string):
    if string is None:
        raise ValueError("String is None.")
    # Clean empty spaces from the right.
    string = string.rstrip()
    if len(string) == 0:
        return 0
    # I know there is at least 1 letter in the string.
    length = 0
    # I want to iterate the string in reverse, since I want the length of the last word.
    for char in string[::-1]:
        # If the char isn't a space, it will be a lowercase of uppercase letter (info told above). There are no !,?,..
        if not char.isspace():
            length += 1
        else:
            break
    return length
