"""

Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question (I Dont know KMP so I will use them)

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.

"""

class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

haystack = "aaaaabbabbaaaababbbbaaabbbaababaababbaabaabaaabbabab"
needle = "bbbaababaa"
sol = Solution()
sol.strStr(haystack=haystack, needle=needle)
# haystack2 = "aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb"
# needle2 = "bba"
# sol.strStr(haystack=haystack2, needle=needle2)