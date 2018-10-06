# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Check if full of zeroes
# Iterate
# Append 0's at the end
# Stop at the length-#zeroes_added position.


class Solution:
    def is_full_of_zeroes(self, nums):
        for num in nums:
            if num != 0:
                return False

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0 or self.is_full_of_zeroes(nums):
            return
        i = 0
        amount_of_zeroes_added = 0
        while i < len(nums) - amount_of_zeroes_added:
            elem = nums[i]
            if elem == 0:
                amount_of_zeroes_added += 1
                del(nums[i])
                nums.append(0)
            else:
                i += 1


