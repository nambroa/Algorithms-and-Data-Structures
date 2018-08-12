"""

LINKED LISTS - QUESTION 2
Implement an algorithm to find the kth to last element of a singly linked list.

Example input: linked_list = 1 --> 2 --> 3 --> 4
Example input: k = 0
Example output: 4 (returns the last element)
Example input: k = 1
Example output: 3 (return the previous to last element)

QUESTIONS:

+ Can the list be empty? Yes, raise exception.
+ Can the list be None or otherwise invalid? No
+ Can the k be invalid? For example larger than the linked list length? Yes, raise exception.
+ Can the k be a fraction or complex? No, it's a positive (including zero) integer.

"""


def get_kth_to_last_element_from(linked_list, k):
    if linked_list.length() == 0:
        raise ValueError("Empty Linked List.")
    first_runner = linked_list.head()
    second_runner = linked_list.head()
    for i in range(k):
        if first_runner is None:
            raise ValueError("Linked List length is not enough to have %s elements." % (k + 1))
        first_runner = first_runner.next_element()
    while first_runner.next_element() is not None:
        first_runner = first_runner.next_element()
        second_runner = second_runner.next_element()
    return second_runner
