"""

LINKED LISTS - QUESTION 5

You have two numbers represented by a linked list, where each node contains a single digit. The digits
are stored in REVERSE order, such that the 1's digit is at the head of the list. Write a function that
adds the two numbers and returns the sum as a linked list

Digits are positive integers, input will be vaild always. --> ASK THIS IN INTERVIEW
Example input: (3 --> 5 --> 8 -->) + (5 --> 1 --> 2) (that's 853 + 215)
Example output: (1 --> 0 --> 6 --> 8) (that's 1068)

"""
from single_linked_list import SingleLinkedList

def at_both_ends(l1_node, l2_node):
    l1_end = l1_node is None or l1_node.next_element() is None
    l2_end = l2_node is None or l2_node.next_element() is None
    return l1_end and l2_end


def is_two_digit_number(number):
    return number / 10 > 0


# PRE: list1 and list2 are not empty and all digits are positive.
def sum_lists(list1, list2):
    current_l1_node = list1.head()
    current_l2_node = list2.head()
    rest = 0
    sum_list = SingleLinkedList.new()
    while current_l1_node is not None or current_l2_node is not None:
        l1_digit = current_l1_node.data() if current_l1_node else 0
        l2_digit = current_l2_node.data() if current_l2_node else 0
        sum = l1_digit + l2_digit + rest
        if is_two_digit_number(sum):
            rest = sum / 10
            sum %= 10
        else:
            rest = 0
        if at_both_ends(current_l1_node, current_l2_node):
            sum_list.insert_data_at_beggining(sum)
            if rest > 0:
                sum_list.insert_data_at_beggining(rest)
            break
        else:
            sum_list.insert_data_at_beggining(sum)
        current_l1_node = current_l1_node.next_element() if current_l1_node else None
        current_l2_node = current_l2_node.next_element() if current_l2_node else None
    return sum_list

# TEST 1
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[1, 2, 3])
list2 = SingleLinkedList.new()
list2.append_from_iterable(iterable=[4, 1, 6])
new_list = sum_lists(list1, list2)
new_list.show()

# TEST 2
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[6, 4, 8])
list2 = SingleLinkedList.new()
list2.append_from_iterable(iterable=[3, 1, 9])
new_list = sum_lists(list1, list2)
new_list.show()

# TEST 3
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[6, 4, 8, 8, 4, 9, 2])
list2 = SingleLinkedList.new()
list2.append_from_iterable(iterable=[3, 1, 9, 3, 5, 7, 8])
new_list = sum_lists(list1, list2)
new_list.show()

# TEST 4
list1 = SingleLinkedList.new()
list1.append_from_iterable(iterable=[2, 3])
list2 = SingleLinkedList.new()
list2.append_from_iterable(iterable=[1])
new_list = sum_lists(list1, list2)
new_list.show()