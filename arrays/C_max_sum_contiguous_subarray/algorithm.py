"""

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

QUESTIONS:

+ Can the array be empty? YES
+ Can the array have negative numbers? YES
+ Can the array be invalid (None or maybe have strings in it)? NO
+ Can you have more than 1 maximum sum? Which one to return? YES, RETURN WHICHEVER ONE.
+ Can the array be all negative? YES What should I return? The maximum number.

"""
import sys


def check_if_all_numbers_are_negative(numbers):
    for number in numbers:
        if number >= 0:
            return False
    return True


def maximum_contiguous_subarray(numbers):
    if numbers is None or len(numbers) == 0:
        raise ValueError("Invalid or otherwise empty array.")
    # First, I check if every number is negative
    if check_if_all_numbers_are_negative(numbers):
        return max(numbers)
    # Otherwise, I return the maximum contiguous subarray.
    current_sum = 0
    maximum_sum = -sys.maxsize
    for i in range(len(numbers)):
        current_sum += numbers[i]
        if current_sum < 0:
            current_sum = 0
        maximum_sum = max(current_sum, maximum_sum)
    return maximum_sum
