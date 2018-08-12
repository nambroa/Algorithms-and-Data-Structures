"""

Given a set of distinct integers, S, return all possible subsets.

Note:
+ Elements in a subset must be in non-descending order.
+ The solution set must not contain duplicate subsets.
+ Also, the subsets should be sorted in ascending ( lexicographic ) order.
+ The list is not necessarily sorted.

Example :
If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def _get_subsets(self, L):
        if len(L) == 0:
            return [[]]
        if len(L) == 1:
            return [[], [L[0]]]
        number_to_append = L[0]
        recursive_subsets = self._get_subsets(L[1:])
        final_subsets = [[]] * len(recursive_subsets)
        for index, subset in enumerate(recursive_subsets):
            final_subsets[index] = [number_to_append] + subset
        recursive_subsets.extend(final_subsets)
        return recursive_subsets

    # If python wasnt this amazing, this is how you would do it. Convert each subset to a string and compare.
    def sort_lexicographically(self, L):
        return sorted(L, key=lambda subset: "".join([str(number) for number in subset]))

    def subsets(self, L):
        L = sorted(L)
        subsets = self._get_subsets(L)
        subsets = sorted(subsets)
        return subsets

