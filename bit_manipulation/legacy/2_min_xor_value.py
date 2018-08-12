"""

Given an array of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

"""

import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A = sorted(A)
        # We first sort the array so we only need to compare consecutive numbers.
        # This is because, for a1 < a2 < a3, a1 and a2 will always have the min xor, since a3 will have more digits
        # since it is higher, therefore having a bigger XOR between it and a1.
        min_xor_value = sys.maxint
        for i in xrange(0, len(A) -1):
            xor_value = A[i] ^ A[i+1]
            min_xor_value = min(xor_value, min_xor_value)
        return min_xor_value