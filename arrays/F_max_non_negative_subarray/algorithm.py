"""

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous.
That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
Sub-array A is greater than sub-array B if sum(A) > sum(B).
If there is a tie between potential subarrays, return one of them.


Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

QUESTIONS:

+ Can the array contain negative numbers? YES
+ Can the array be ALL negative? YES What should I return then? -1
+ Can the array be empty or None? YES
+ Can the array be invalid? NO
+ Are all the numbers from the array integers or otherwise real? YES

"""


def maximum_non_negative_subarray(numbers):
    best_candidate = []
    current_sum = 0
    max_sum = 0
    candidate = []
    for number in numbers:
        if number < 0 and current_sum >= 0:
            if current_sum >= max_sum:
                best_candidate = candidate
                max_sum = current_sum
            current_sum = 0
            candidate = []
        elif number >= 0:
            current_sum += number
            candidate.append(number)
    # Last iteration
    if current_sum > max_sum:
        best_candidate = candidate
        max_sum = current_sum
    return best_candidate
