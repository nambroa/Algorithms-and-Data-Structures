# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Your algorithm should have a linear runtime complexity. Can you do it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution:
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appearances_hashmap = self._make_appearances_hashmap_from(nums)
        for number, number_of_appearances in appearances_hashmap.items():
            if number_of_appearances == 1:
                return number

    def _make_appearances_hashmap_from(self, nums):
        hashmap = {}
        for num in nums:
            try:
                hashmap[num] += 1
            except KeyError:
                hashmap[num] = 1
        return hashmap
