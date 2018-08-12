"""

Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.

"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def add_number_to_all_posible_places_of_list(self, number, L):
        n = len(L)
        permutations = [[]] * (n + 1)
        for i in xrange(0, len(permutations)):
            new_permutation = L[0:i] + [number] + L[i:n]
            permutations[i] = new_permutation
        return permutations

    def permute(self, L):
        # Check for empty list edge case and Base recursion case.
        if len(L) == 0:
            return []
        if len(L) == 1:
            return [[L[0]]]
        # I select the first number and add it to all possible places of the rest of the permutations.
        number_to_add = L[0]
        permutations = self.permute(L[1:])
        finished_permutations = []
        for permutation in permutations:
            new_permutations = self.add_number_to_all_posible_places_of_list(number_to_add, permutation)
            finished_permutations.extend(new_permutations)
        return finished_permutations


sol = Solution()
sol.permute([1, 2, 3])
