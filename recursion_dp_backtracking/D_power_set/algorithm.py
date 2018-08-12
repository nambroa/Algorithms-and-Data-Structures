"""

Write a method to return all subsets of a set.
EXAMPLE: If input = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ In what datastruct will the input be? List
+ Can the set be empty? Yes, return [[]]
+ Can the input be None? Yes, raise exc.
+ Can the set contain anything other than integers? No
+ Can the set contain repeated numbers? No (CRUCIAL)

"""

"""

Caveat: new_subsets.extend(subsets) is O(|subsets|)
Complexity: (N * (2^N))
Explanation: A set S will have |2^N| subsets in a power set. Each iteration is, at worst, N.

"""


def _get_all_subsets_of(numbers):
    if not numbers:
        return [[]]  # Base case.
    else:
        last_number = numbers[-1]
        subsets = _get_all_subsets_of(numbers[0:len(numbers)-1])
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [last_number])
        new_subsets.extend(subsets)
        return new_subsets


def get_all_subsets_of(numbers):
    if numbers is None:
        raise ValueError("Numbers are None.")
    if len(numbers) == 0:
        return [[]]
    return _get_all_subsets_of(numbers)