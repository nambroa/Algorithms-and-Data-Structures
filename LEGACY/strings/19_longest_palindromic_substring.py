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

"""

"""

First, a naive solution that works really well thanks to yield. Worst case if when the longest palindrome is
just one char, which forces it to return all the substrings up to that moment and checking for palindrome, which
is O(n^3).

"""


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        for substring in self.substrings(A):
            if self.palindrome(substring):
                return substring

    def palindrome(self, s):
        return s[len(s) / 2:] == s[(len(s) - 1) / 2:: -1]

    def substrings(self, s):
        n = len(s)
        # Here I chose range over xrange for python version compatibility.
        for end in range(n, 0, -1):
            for i in range(n - end + 1):
                # We return the substrings, starting from the longest ones possible.
                # For example, the first iteration end = 5, i = 0.
                # The second one, end = 4, and i = 0, 1. We start from the longest possible ones.
                # Since we use yield, we give the substrings as we need them (iterating the for loop), saving time.
                # This is because yield returns a generator, not another iterable like a list.
                yield s[i: i + end]

"""

After that, another more complex solution that has O(n^2) runtime

Basic thought is simple, when you increase s by 1 character, you could only increase your maximum palindrome length
by 1 or 2, and that new maximum palindrome includes the new character. You can never increase a palindrome by
more than 2 chars.

So, you only need to scan from beggining to end, adding one character at a time, keeping track of the maximum
palindrome length, and for each added character, you check if the substrings ending with this character, with
length P+1 and P+2, are palindromes. If they are, you update the maximum palindrome and it's length.

This is O(n^2). O(n) for the for loop. Inside the loop, we do slicing + palindrome check, which is O(n).

Hacer corrida a mano con "xcbabaqd" o "xcbabaqdbababkj" para entender. "cbbd" para entender el i - maxlen >= 0.
"""


class BetterSolution:

    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in xrange(1, len(s)):
            # Check if starting index should be i-maxLen or i-maxLen-1.
            # Important: if s[i-maxLen-1: i+1] is a palindrome, when you update maxLen, s[i - maxLen:i + 1] will not be
            # a palindrome, so you never extend maxLen more than necessary.
            if i - maxLen >= 1:  # If it needs to check around the last substring.
                substring = s[i-maxLen-1: i+1]
                if self.is_palindrome(substring):
                    start = i - maxLen - 1
                    maxLen += 2
            if i - maxLen >= 0:  # Check inside the last substring.
                substring = s[i - maxLen:i + 1]
                if self.is_palindrome(substring):
                    start = i - maxLen
                    maxLen += 1
        return s[start:start + maxLen]

    def is_palindrome(self, s):
        return s[len(s) / 2:] == s[(len(s) - 1) / 2:: -1]


sol = Solution()
sol.longestPalindrome("babad")
bettersol = BetterSolution()
bettersol.longestPalindrome("cbbd")

"""

A maybe easier to understand Java solution, expanding around its center.
we could solve it in O(n^2) time using only constant space.

We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.

You might be asking why there are 2n - 1 but not n centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters ('abba') and its center are between the two 'b's

public String longestPalindrome(String s) {
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}


What this function does is, as long as we are "in a palindrome" (aka s.charAt(L) == s.charAt(R)), expand around that.
Then, return the length of the palindrome (R - L - 1) osea end - beggining - 1
private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}

"""

class MagnificentSolution(object):
    def longest_palindromic_substring(self, string):
        if len(string) < 1: return -1
        n = len(string)
        start = end = 0
        current_len = 1
        for i in range(n):
            start_1, end_1, len_1 = self.find_palindrome_length_expanding_around_center(string, i, i)
            start_2, end_2, len_2 = self.find_palindrome_length_expanding_around_center(string, i, i+1)
            start_end_indexes_map = {len_2: [start_2, end_2], len_1: [start_1, end_1]}
            max_len = max(len_1, len_2)
            if max_len > current_len:
                start = start_end_indexes_map[max_len][0]
                end = start_end_indexes_map[max_len][1]
                current_len = end - start
        if start == 0 and end == 0: return -1  # Case when no palindrome was found
        return string[start+1:end]

    def find_palindrome_length_expanding_around_center(self, string, start, end):
        start_index = start
        end_index = end
        while start_index >= 0 and end_index < len(string) and string[start_index] == string[end_index]:
            start_index -= 1
            end_index += 1
        return start_index, end_index, end_index-start_index-1

sol = MagnificentSolution()
print(sol.longest_palindromic_substring("kcabba"))
print(sol.longest_palindromic_substring("rekcabbamuyopllpo"))
print(sol.longest_palindromic_substring("rekcabbamuyopllporehdpoiuyttyuiopmty"))