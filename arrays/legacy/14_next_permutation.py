# coding=utf-8
"""

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50

IMPORTANT EXAMPLE:
1,3,2 -> 2,1,3

QUESTIONS YOU SHOULD ASK:

+ Can input be valid/is the list sorted.
+ Can it contain negative numbers? Yes. What should I do with them? Treat them as positive.

"""


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        lower_index = -1
        n = len(A)
        # We search for the first index that meets the property A[i] < A[i+1].
        # This means it's the first number that is followed by a bigger one.
        # We search from the end because we need to find the first index of "smallest digit value".
        for i in range(n - 2, -1, -1):
            if A[i] < A[i + 1]:
                lower_index = i
                break
        # If I can't find one, the array is sorted in descending, so there is no possible permutation.
        # I return the same array, but sorted in ascending order.
        if lower_index == -1:
            return sorted(A)
        higher_index = lower_index + 1
        left = lower_index + 1
        # We search A starting from the right of the index of lower_index, because we know those elements are in
        # descending order and are of the smallest digit value (so that we find the next greatest permutation and not
        # the greatest one).
        # Looking to the left makes no sense because swapping with one of those would make for a bigger permutation
        # Than just swapping A[i] and A[i+1], that have lower "digit values".
        # We are searching for an element that is "just a bit bigger" than A[lower_index].
        # In case we can't find it, A[higher_index] will always be greater than A[lower_index], because it's the pair
        # we found at the first for. (that's why we start from left+1 as well)
        for i in range(left + 1, n):
            if A[lower_index] < A[i] < A[higher_index]:
                higher_index = i
        # We swap.
        A[lower_index], A[higher_index] = A[higher_index], A[lower_index]
        # We merge, taking into consideration that we already know that A[lower_index+1:] it's on descending order.
        # We just need that part to be in ascending order in order to have the next greater permutation.
        A = A[:lower_index + 1] + sorted(A[lower_index + 1:])
        return A

sol = Solution()
A = [3, 1, 1, 5, 6, 2]
print(sol.nextPermutation(A))
