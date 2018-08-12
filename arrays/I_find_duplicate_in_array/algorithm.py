"""

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less
than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1

QUESTIONS YOU COULD ASK:
+ Can the list come empty? Yes
+ Can the input be invalid? (since python isn't strongly-tiped you could give something other than a list) No
+ In this exercise, positive/negative/zero integers are the same, but those are usually good things to ask.

"""


def find_duplicate_in_list(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("No numbers found.")
    appearances_set = set()
    # the range is going to be 0...n-1 so that I don't accidentally use O(n) space in the worst case.
    for i in range(len(numbers)-1):
        if numbers[i] in appearances_set:
            return numbers[i]
        else:
            appearances_set.add(numbers[i])
    if numbers[-1] in appearances_set:
        return numbers[-1]
    return -1