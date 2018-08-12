"""

Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,
1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
2. Entries should be sorted within themselves.

Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]

 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.

"""


class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        # Cover edge cases
        if n < k:
            return []
        if n == k:
            list_of_1_to_n = [range(1, n+1)]
            return list_of_1_to_n

        # Cover base case
        if k == 1:
            return [[x] for x in range(1, n+1)]

        # Recursive algorithm
        new_combinations = []
        previous_combinations = self.combine(n-1, k-1)
        for combination in previous_combinations:
            last_number = combination[-1]
            for num in xrange(last_number + 1, n+1):
                new_combinations.append(combination + [num])
        return new_combinations

sol = Solution()
sol.combine(n=5, k=3)