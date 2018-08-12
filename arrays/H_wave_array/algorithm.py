"""

Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

EXAMPLE:
    Given [1, 2, 3, 4]

    One possible answer : [2, 1, 4, 3]
    Another possible answer : [4, 1, 3, 2]

PLEASE NOTE:
If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]

QUESTIONS YOU SHOULD ASK:
+ Is the input always going to be valid? Yes.
+ Can I get zeroes or negatives in the list? Yes
+ Does the array come sorted? No
+ Can the list have repeated numbers? No

"""


def create_wave_list_from(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("Numbers list is empty or otherwise invalid.")
    numbers = sorted(numbers)
    i = 0
    # I want to iterate through all the numbers except the last one, which will be moved in the last iteration.
    while i < len(numbers) - 1:
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp
        i += 2
    return numbers
