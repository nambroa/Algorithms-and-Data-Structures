"""

You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.


QUESTIONS:

+ Can the array be empty, None, or have invalid characters? NO
+ Can the array have complex numbers? NO
+ Can the array have only one number? NO

EXAMPLE: A=[1, 3, -1]

All possible f's are as follows:

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.

"""

"""
Idea: understand the properties of absolute values. f(i,j) can be written in 4 ways.

Case 1: A[i] > A[j] and i > j
|A[i] - A[j]| = A[i] - A[j]
|i -j| = i - j
hence, f(i, j) = (A[i] + i) - (A[j] + j)

Case 2: A[i] < A[j] and i < j
|A[i] - A[j]| = -(A[i]) + A[j]
|i -j| = -(i) + j
hence, f(i, j) = -(A[i] + i) + (A[j] + j)

Case 3: A[i] > A[j] and i < j
|A[i] - A[j]| = A[i] - A[j]
|i -j| = -(i) + j
hence, f(i, j) = (A[i] - i) - (A[j] - j)

Case 4: A[i] < A[j] and i > j
|A[i] - A[j]| = -(A[i]) + A[j]
|i -j| = i - j
hence, f(i, j) = -(A[i] - i) + (A[j] - j)

Note that case 1 and 2 are equivalent and so are case 3 and 4 and hence we can design our algorithm only
for two cases as it will cover all the possible cases.

"""


def maximum_absolute_difference(numbers):
    N = len(numbers)
    sum_part = [numbers[i] + i for i in range(N)]
    sub_part = [numbers[i] - i for i in range(N)]
    max_sum, min_sum = max(sum_part), min(sum_part)
    max_sub, min_sub = max(sub_part), min(sub_part)
    return max(max_sum - min_sum, max_sub - min_sub)

