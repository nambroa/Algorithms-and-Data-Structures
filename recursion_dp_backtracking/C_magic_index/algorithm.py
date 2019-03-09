"""

A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in an array A.

FOLLOW UP: What if the values are not distinct?

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes?
+ Will the input always valid? (aka an array)
+ Are the integers always positive? No
+ Do the indexes such that A[i] = i start from 0? Yes

"""

"""

Initial algorithm

Basically binary search.

Some clarifications on complexity:

The performance of binary search can be analyzed by reducing the procedure to a binary comparison tree. 
The root node of the tree is the middle element of the array. The middle element of the lower half is 
the left child node of the root and the middle element of the upper half is the right child node of the root. 

The rest of the tree is built in a similar fashion. This model represents binary search. Starting from 
the root node, the left or right subtrees are traversed depending on whether the target value is less or more than 
the node under consideration. This represents the successive elimination of elements, making it a complexity of
worst case O(log(n)+1) in the end.

"""


def _find_magic_index_in(numbers, start, end):
    middle_point = int((start + end) / 2)
    middle_array_value = numbers[middle_point]
    if start > end:
        return None
    if middle_array_value == middle_point:
        return middle_point
    if middle_array_value > middle_point:
        return _find_magic_index_in(numbers, start, middle_point - 1)
    if middle_array_value < middle_point:
        return _find_magic_index_in(numbers, middle_point + 1, end)


def find_magic_index_in(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("No array found or empty array.")
    return _find_magic_index_in(numbers=numbers, start=0, end=len(numbers) - 1)


"""

Final note: When calling _find_magic_index_in for the first time, passing len in place of len-1 won't change much. 
If len is odd then len-1 will be even and both will give same mid value.
If len is even then you have two elements in mid position. Passing len-1 will give us the first mid point, while
passing len will give the second one.

"""

"""

Follow-up algorithm


The idea is to do the same as above, but try to skip the repeated values.
Since there can be many repeated values, I need to search both sides all the time. For example with
[0, 2, 2, 2, 2, 2, 2, 2, 99, 100], the answer is on the left but the normal algorithm tells me to go right.

However, how do I know which parts to search for? We should use 2 facts
A) The array is sorted.
B) There may be (multiple) repeats.

For the left, I want to start from the index that's min between middle_point-1 and middle_array_value.
EXAMPLE 1:
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 99, 100]
A[mid] = A[6] = 2
If I do the recursion between indexes 0 and 6, it's pointless from the indexes 3-6 since I already know they will be
of value 2 or lower. I need the recursion between indexes 0 and 2, which guarantees me that there may be a magic index
hiding in any of those indexes (because A[2] can be 2 or lower, for example).

EXAMPLE 2:
[0, 1, 6, 6, 6, 7, 8, 9, 99]
A[mid] = A[4] = 6
If I do the recursion between indexes 0 and 6, it's pointless from the indexes 4 to 6 since I will be searching those
in the right part of the recursion (because since A[4]=6, A[6] could be 6 too!). Doing it from indexes 0 to 4 allows me
to find a magic index that's below 6. A[5] is always pointless since it will be 6 or more, therefore not a magic index.

For the right, it's the same logic but using max(middle_point+1, middle_array_value).

"""


def _find_follow_up_magic_index_in(numbers, start, end):
    if not numbers:
        return None
    if end < start:
        return False
    middle_point = int((start + end) / 2)
    middle_array_value = numbers[middle_point]
    if middle_array_value == middle_point:
        return middle_point

    # Search left
    left_index = min(middle_point - 1, middle_array_value)
    left = _find_follow_up_magic_index_in(numbers, start, left_index)
    if left:
        return left

    # Search right
    right_index = max(middle_point + 1, middle_array_value)
    right = _find_follow_up_magic_index_in(numbers, right_index, end)
    if right:
        return right


def find_follow_up_magic_index_in(numbers):
    if not numbers or len(numbers) == 0:
        raise ValueError("No array found or empty array.")
    return _find_follow_up_magic_index_in(numbers=numbers, start=0, end=len(numbers) - 1)
