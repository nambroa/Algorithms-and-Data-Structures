# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


import math


class Solution:
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appearances_hashmap = {}
        for num in nums:
            try:
                appearances_hashmap[num] += 1
            except KeyError:
                appearances_hashmap[num] = 1
        for num, amount_of_appearances in appearances_hashmap.items():
            if amount_of_appearances > (math.floor(len(nums)/2)):
                return num

