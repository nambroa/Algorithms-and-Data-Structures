"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

"""

Remember the array is sorted, except it might drop at one point.

If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element, and in case of "<" there
must be a drop elsewhere). So we should keep searching in nums[0..i] if the target lies in this sorted range, i.e.,
if nums[0] <= target <= nums[i].). This is the case "end = mid".

If nums[0] > nums[i], then nums[0..i] contains a drop, and thus nums[i+1..end] is sorted and lies strictly between
nums[i] and nums[0]. So we should keep searching in nums[0..i] if the target doesn't lie strictly between them, i.e.,
if target <= nums[i] < nums[0] or nums[i] < nums[0] <= target

"""


class Solution(object):
    def search(self, nums, target):
        begin, end = 0, len(nums) - 1
        while begin < end:
            mid = (begin + end) / 2
            if (nums[0] <= target <= nums[mid]) or (nums[0] > nums[mid] and (target >= nums[0] or target <= nums[mid])):
                end = mid
            else:
                begin = mid + 1
        return begin if target in nums[begin:begin+1] else -1


