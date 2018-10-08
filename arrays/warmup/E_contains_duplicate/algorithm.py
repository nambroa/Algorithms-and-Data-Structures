# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return
# false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


class Solution:

    def make_appearances_hashmap_of(self, numbers):
        hashmap = {}
        for number in numbers:
            try:
                hashmap[number] += 1
            except KeyError:
                hashmap[number] = 1
        return hashmap

    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = self.make_appearances_hashmap_of(nums)
        for number, amount_of_appearances in hashmap.items():
            if amount_of_appearances > 1:
                return True
        return False
