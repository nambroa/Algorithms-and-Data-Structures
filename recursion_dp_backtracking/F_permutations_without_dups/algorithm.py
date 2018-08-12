"""

Write a method to compute all permutations of a string of UNIQUE characters.

Example: "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]

QUESTIONS YOU SHOULD ASK:

+ Can the string be empty? In that case, what do you want me to return? ""
+ Can the input be None? What should I return? Yes, raise exc.
+ Can I recieve something else/should I sanitize? No

"""

"""

The idea is similar to Power Set.

For 'ABC', we have 6 permutations.
For 'ABCD', we have 24 permutations.
For 'ABCDE', we have 120 permutations.
For 'ABCDEF', we have 720 permutations.


We can see that the output grows exponentially with the input, at a rapid rate.
For a given string of length N, there are N! permutations.
It takes around N to obtain one (since we have to iterate over previous permutations).

Total: O(N! * N)
"""


def get_all_permutations_of(string):
    if string is None:
        raise ValueError("String is None.")
    if len(string) == 0:
        return ''
    first_char = string[0]
    permutations = get_all_permutations_of(string[1:len(string)])
    new_permutations = []
    if permutations == '':
        return [first_char]
    for permutation in permutations:
        # I want to add the char in each possible space
        for i in range(len(permutation) + 1):
            new_permutation = permutation[:i] + first_char + permutation[i:]
            new_permutations.append(new_permutation)
    return new_permutations
