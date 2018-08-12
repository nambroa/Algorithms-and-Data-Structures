"""

---------------------------------- Cracking the Coding Interview ----------------------------------


ARRAY AND STRINGS - QUESTION 6
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string "aabcccccaaa" would become "a2b1c5a3".
If the "compressed" string would not become smaller than the original, return the original string.

QUESTIONS:

+ Can the string be empty or None? Can the input be invalid? No, you can assume input will be 100% sanitized!
+ Can the string contain numbers? No
+ Can the string contain uppercase letters? If so, how should I treat them? The string will only contain lowercase.
+ Can the string contain spaces? No. If it had them, you would need to sanitize them.

"""


"""

The idea is to iterate over the string. We store the previous iterated letter and the amount of times we saw it
before a new letter came up. Each time the current letter is different, we store in the compressed string something
like "previous_letter + amount_of_appearances_it_had".

Since we iterate over all the string, and each iteration is full of O(1) operations, runtime complexity is O(|string|).

"""


def compress_string(s1):
    if len(s1) == 1:
        return s1
    compressed_string = ''
    previous_letter = s1[0]
    amount_of_aps = 1
    for word in s1[1:]:
        if word == previous_letter:
            amount_of_aps += 1
        else:
            compressed_string = compressed_string + previous_letter + str(amount_of_aps)
            previous_letter = word
            amount_of_aps = 1
    # I need to do the last iteration by hand.
    compressed_string = compressed_string + previous_letter + str(amount_of_aps)
    if len(compressed_string) < len(s1):
        return compressed_string
    else:
        return s1
