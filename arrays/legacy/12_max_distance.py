"""

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)


"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        maximum_gap = -1
        # If the array only has one element, there is no possible distance between the two.
        if n == 1:
            return maximum_gap
        Lmin = [0] * n
        Rmax = [0] * n
        # Lmin[0] has the first elem of A, and for Lmin[i] it will have A[i] if it's lower than the previous one
        # The idea is that Lmin contains all the potential min candidates in their respective positions of A.
        # Lmin[i] will tell you if a new max has been found at A[i] or not. If it hasn't, it will show Lmin[i-1]
        Lmin[0] = A[0]
        for i in range(1, n):
            Lmin[i] = min(Lmin[i - 1], A[i])
        # Rmax[n-1] has the last elem of A, and for Rmax[i] it will have A[n-i] if it's higher than the previous one.
        # The idea is that Rmax contains all the potential max candidates in their respective positions of A.
        # Rmax[i] will tell you if a new max has been found at A[n-i] or not. If it hasn't, it will show Rmax[i-1]
        Rmax[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            Rmax[i] = max(Rmax[i + 1], A[i])
        i = 0
        j = 0
        # Now we iterate both at the same time and find the maximum possible distance for all the min/max candidates.
        while i < n and j < n:
            if Lmin[i] <= Rmax[j]:
                maximum_gap = max(maximum_gap, j - i)
                j += 1
            else:
                i += 1
        return maximum_gap

sol = Solution()
A = [3, 5, 4, 2, 9]
print(sol.maximumGap(A))