# coding=utf-8
"""

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where  A,B,C and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0. That means '0' is the only valid "ip part" that can be zero.
'00', '000' are not valid.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)

"""


class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        A = A.strip()
        n = len(A)
        if 12 < n < 4:
            # Invalid length for ip address.
            return []
        ret = []
        i = 1
        while i <= 3 and i < n:
            j = i+1
            while j <= i + 3 and j < n:
                k = j + 1
                while k <= j + 3 and k < n:
                    # First part of the ip
                    a = int(A[:i])
                    # Second part of the ip
                    b = int(A[i:j])
                    # Third part of the ip
                    c = int(A[j:k])
                    # Fourth part of the ip
                    d = int(A[k:])
                    # If A[0] == '0' and i > 1 --> That part of the ip is longer than 1, so the zero is invalid.
                    if (A[0] == '0' and (i > 1 or a != 0)) or (A[i] == '0' and (j > i+1 or b != 0)) or (A[j] == '0' and (k > j + 1 or c != 0)) or (A[k] == '0' and (n > k+1 or d != 0)):
                        # Do Nothing
                        k += 1
                        continue
                    elif 255 >= a >= 0 and 255 >= b >= 0 and 255 >= c >= 0 and 255 >= d >= 0:
                        ret.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
                    k += 1
                j += 1
            i += 1
        return ret

sol = Solution()
sol.restoreIpAddresses("25525511135")