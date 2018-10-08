# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.


class Solution:
    def make_appearances_hashmap_of(self, s):
        hashmap = {}
        for char in s:
            try:
                hashmap[char] += 1
            except KeyError:
                hashmap[char] = 1
        return hashmap

    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # What we want to know is if s and t have the same letters in the same amount.
        # First, the easiest way to discard strings is by length comparison. They have to be equal.
        if s is None or t is None or len(s) != len(t):
            return False
        # We make a hashmap out of the letters in s.
        appearances_hashmap = self.make_appearances_hashmap_of(s)
        # We iterate over the hashmap, removing entries that match with chars of t.
        # At the end, the hashmap must be empty. There must be no Key Errors as well.
        for char in t:
            try:
                appearances_hashmap[char] -= 1
                if appearances_hashmap[char] < 0:
                    return False
            except KeyError:
                return False
        return True
