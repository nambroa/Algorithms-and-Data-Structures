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

Please Note:
+ No two entries in the permutation sequence should be the same.
+ For the purpose of this problem, assume that all the numbers in the collection are unique.
+ The order in which you return the permutations does not matter.

"""


# This seems like a recursive problem. Let's try to do recursion on the numbers.
# We should think about base and recursive cases.
# For the base case, we can say that the permutation of [a] will always be [a].
# Now, let's say we have all the permutations of [1,2], which would be [1,2] and [2,1]
# We want to now obtain all the permutations of [1,2,3]. How can we use the permutations from [1,2]?

# What we can do is insert the number "3" in every space available of all the permutations of [1,2].
# For example, inserting "3" in every space available of [2,1] would yield [3,2,1], [2,3,1], [2,1,3]

# To understand the time complexity of this algorithm, we need to analyze a few variables
# 1) The call tree (recursive stack) is O(N), since we make 3 calls for [1,2,3] (list of length 3).
# 2) Every recursive call, the function iterates at most (N-1) permutations.
# 3) Every iteration of the permutation, the function creates at most N arrays. Then, it extends with those N.
# Final complexity: O(N*N*N)

def add_number_in_all_available_spaces(last_number, previous_permutation):
    new_permutations = []
    for index in range(len(previous_permutation)+1):
        new_permutation = previous_permutation[:index] + [last_number] + previous_permutation[index:]
        new_permutations.append(new_permutation)
    return new_permutations


def _get_all_permutations(numbers, current_permutations):
    if len(numbers) == 1:
        return [numbers]
    last_number = numbers[-1]
    previous_permutations = _get_all_permutations(numbers[0:len(numbers) - 1], current_permutations)
    all_permutations = []
    for previous_permutation in previous_permutations:
        new_permutations = add_number_in_all_available_spaces(last_number, previous_permutation)
        all_permutations.extend(new_permutations)
    return all_permutations


def get_all_permutations(numbers):
    if numbers is None:
        raise ValueError("Numbers are None or empty.")
    if len(numbers) == 0:
        return numbers
    return _get_all_permutations(numbers, [])
