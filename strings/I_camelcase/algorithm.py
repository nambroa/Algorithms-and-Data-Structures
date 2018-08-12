"""

Alice wrote a sequence of words in CamelCase as a string of letters, S, having the following properties:

+ It is a concatenation of one or more words consisting of English letters.
+ All letters in the first word are lowercase.
+ For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
+ Given S, print the number of words in S on a new line.

QUESTIONS:

+ Can S be None or empty, or otherwise invalid? Ycan assume that the input is valid and sanitized. It can be empty.
+ Can S have spaces? Yes, you should clean them.

"""


def _clean_whitespaces_from(string):
    string = ''.join([word for word in string if not word.isspace()])
    return string


def amount_of_words_in_camelcase(camelcase):
    camelcase = _clean_whitespaces_from(camelcase)
    if len(camelcase) == 0:
        return 0
    # If the list would be too big to handle, you can always do a classic for loop.
    amount_of_uppercase_letters = [letter for letter in camelcase if letter.isupper()]
    return len(amount_of_uppercase_letters) + 1  # +1 because the first word is all lowercase
