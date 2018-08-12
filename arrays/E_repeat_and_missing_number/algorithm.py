"""

You are given a read only array of n integers from 1 to n. The array is NOT sorted.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.


QUESTIONS:

+ Will A and B always exist? YES
+ Can the array be empty? YES
+ Can the array be None? YES
+ Can the array be invalid? NO

"""


def get_repeated_number_from(numbers):
    unique_numbers = set()
    for number in numbers:
        if number in unique_numbers:
            return number
        unique_numbers.add(number)


def get_repeated_and_missing_number(numbers):
    if numbers is None or len(numbers) == 0:
        raise ValueError("No array of numbers found.")
    repeated = get_repeated_number_from(numbers)
    numbers.remove(repeated)
    sum_of_current_numbers = sum(numbers)
    N = max(numbers)
    # Theorem: sum(1,n) = n(n+1)/2
    maximum_sum = ((N*(N+1))/2)
    # We should check whether or not the array is missing its last number.
    if maximum_sum == sum_of_current_numbers:
        # If no number in the array is missing, and B always exists, it has to be that it's missing its last number.
        return repeated, N+1
    else:
        return repeated, maximum_sum - sum_of_current_numbers
