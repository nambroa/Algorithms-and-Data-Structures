# coding=utf-8

"""

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

QUESTIONS:

+ What should I return if I don't find a palindromic substring? Return -1
+ Can the input be invalid? No
+ Can the input be empty? Yes, in this case return -1.

"""

"""

One of the best solutions consists on the concept of expanding around the "center" of the word.
The "center" is a point in the word from where the palindrome can mirror around. So there are multiple centers per word.
With this technique, we can solve the problem in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.

You might be asking why there are 2n - 1 but not n centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters ('abba') and its center are between the two 'b's

"""


def longest_palindromic_substring(string):
    # Palindrome words need to have at least 2 letters, by definition.
    if len(string) < 1: return -1
    n = len(string)
    start = end = 0
    current_len = 1
    # We iterate to find the largest palindromic substring, expanding around 2n-1 centers.
    for i in range(n):
        start_1, end_1, len_1 = find_palindrome_length_expanding_around_center(string=string, start=i, end=i)
        start_2, end_2, len_2 = find_palindrome_length_expanding_around_center(string=string, start=i, end=i+1)
        start_end_indexes_map = {len_2: [start_2, end_2], len_1: [start_1, end_1]}
        max_len = max(len_1, len_2)
        if max_len > current_len:
            start = start_end_indexes_map[max_len][0]
            end = start_end_indexes_map[max_len][1]
            current_len = end - start
    if start == 0 and end == 0: return -1  # Case when no palindrome was found
    return string[start+1:end]


def find_palindrome_length_expanding_around_center(string, start, end):
    # This function expands around the start index of the string. In every step, it checks if the current expansion
    # is a palindrome. When this check fails, the function returns the indexes neccesary to form the palindrome found.
    start_index = start
    end_index = end
    while start_index >= 0 and end_index < len(string) and string[start_index] == string[end_index]:
        start_index -= 1
        end_index += 1
    return start_index, end_index, end_index-start_index-1