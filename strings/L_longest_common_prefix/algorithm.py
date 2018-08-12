"""

Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? No, it can be empty list or None
+ What should I return when I don't find any common prefix? Empty string ""

"""

"""

The idea is to start with the string of maximum length and check for longest common prefix iteratively.

"""


def find_longest_common_prefix_between(strings):
    if not strings or len(strings) == 0:
        raise ValueError("No strings found.")
    longest_common_prefix = ''
    current_common_prefix = ''
    string_of_min_length = min(strings, key=len)
    # Iterate through the chars of the min_string. If it's a match for all other strings, add it to the current prefix.
    for i in range(len(string_of_min_length)):
        current_char = string_of_min_length[i]
        is_prefix_of_all_strings = True
        for string in strings:
            if string[i] != current_char:
                # Common prefix has ended. I store it if it's longer than my current maximum.
                is_prefix_of_all_strings = False
                longest_common_prefix = max(longest_common_prefix, current_common_prefix, key=len)
                current_common_prefix = ''
        # All strings have it in common
        if is_prefix_of_all_strings:
            current_common_prefix += current_char
    longest_common_prefix = max(longest_common_prefix, current_common_prefix, key=len)
    return longest_common_prefix
