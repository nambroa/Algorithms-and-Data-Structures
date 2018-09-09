"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.

QUESTIONS:

+ Can the input be empty or invalid? It can be empty but not invalid. In case of empty, return empty string.
+ What if the string only has 1 char of non repeating characters? Return that same char.
+ Can I get a string that has multiple longest substrings? Yes, you can return any of those.

"""

"""

For our entry point, we can see that every substring has one starting index from 0 to len(string). The ending index
can vary, but since we are looking for the longest one, we know that it will only have one ending index.

Following that logic, we can iterate the string from 0 to len(string) starting indexes. In each iteration, we try
to expand the substring as much as possible without repeating characters.

This gives us a complexity of O(n^2) at worst. Optimizations can be made. For example, if we find that the whole word
is one substring without repeating characters, there is no need to search further. With that reasoning, if the current
longest substring is larger or equal than len(string) - (next starting index).

We can lower the complexity to O(n). Instead of resetting the search each time we get a new starting index,
when we can't expand the substring any further, we move the starting index to the smallest position available so we
have the next substring, and we continue from there. This gives us a total complexity of around O(n).

"""


def longest_substring_without_repeating_characters(string):
    maximum_length = 0
    start_index = 0
    already_found_chars = {}
    for i in range(len(string)):
        if string[i] in already_found_chars and start_index <= already_found_chars[string[i]]:
            # If the current char is already used in the current substring, we move the start index to a point
            # in the string where it's no longer used, so we avoid it's repetition.
            # We don't care about the case where the starting index is after the usage of the current char, since
            # that implies that it is not part of the current substring.
            start_index = already_found_chars[string[i]] + 1
        else:
            current_substring_length = i - start_index + 1
            maximum_length = max(maximum_length, current_substring_length)
        # We record the last time we saw the current char, in order to ensure we won't repeat it
        # in the current substring.
        already_found_chars[string[i]] = i
    return maximum_length































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
