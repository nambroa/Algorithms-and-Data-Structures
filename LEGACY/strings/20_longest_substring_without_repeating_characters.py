"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.



"""


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1  # Es +1 porque empiezo en el lugar siguiente de donde lo vi x ultima vez.
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i

        return maxLength

sol = Solution()
sol.lengthOfLongestSubstring("abba")


