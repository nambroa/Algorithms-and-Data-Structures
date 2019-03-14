# Given a column title as appears in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701

# The amount that each letter is "worth" in numbers is tied to its position in the string.
# A = 1, but AA has the first A worth 26 and the second one worth 1.


class Solution:
    def map_letter_to_column_number(self, letter):
        return ord(letter) - 64

    def title_to_number(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        s = s.upper()
        if len(s) == 1:
            return self.map_letter_to_column_number(s)
        number = 0
        for index, letter in enumerate(s[0:-1]):
            number += pow(26, len(s) - (index + 1)) * self.map_letter_to_column_number(letter)
        number += self.map_letter_to_column_number(s[-1])
        return number
