"""

Implement strStr().

strstr - locate a substring (needle) in a string (haystack).

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

QUESTIONS:

+ Can the substring be empty? What should I return? Yes, return -1.
+ Can the string be empty? What should I return? Yes, return -1.

"""

"""

The idea is to iterate the main string only up to len(string) - len(substring) + 1. Because after that length, there
is no chance to find the substring. For example, if string = 'aaabbaaa' with length 8 and substring = 'baa' with length
3, you would iterate the main string up to the index 6. That means up to 'aaabba'. If we would iterate over the
remaining two chars, we would never find the substring since its length is 3.

For each i that we iterate over, we want to see if we can find the substring over there. Using the example above,
with i=0, we would like to see if string[0:3] is 'baa'. If we don't find it, we need to check [1:4], and so on..

"""


def locate_substring_in_string(substring, string):
    if not string or not substring:
        return -1
    for i in range(len(string) - len(substring) + 1):
        if string[i: i + len(substring)] == substring:
            return i
    return -1
