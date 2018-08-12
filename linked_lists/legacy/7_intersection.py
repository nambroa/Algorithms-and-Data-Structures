"""

LINKED LISTS - QUESTION 7

Given two single linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on REFERENCE, not DATA VALUE.
That is, the kth node of the first list has to be the exact same node (object) as the jth node of the 2nd list.

Nodes can contain integers. Input will be valid. --> ASK THIS IN INTERVIEW

"""
from single_linked_list import SingleLinkedList, SingleLinkedNode


def validate_input(list1, list2):
    current_list1_node = list1.head()
    current_list2_node = list2.head()
    if not current_list1_node or not current_list2_node:
        return False


def make_ids_hashset_from(list1):
    ids_hashset = set()
    current_list1_node = list1.head()
    while current_list1_node is not None:
        ids_hashset.add(id(current_list1_node))
        current_list1_node = current_list1_node.next_element()
    return ids_hashset


def intersection(list1, list2):
    validate_input(list1, list2)
    ids_hashset = make_ids_hashset_from(list1)
    current_list2_node = list2.head()
    while current_list2_node is not None:
        if id(current_list2_node) in ids_hashset:
            return True
        current_list2_node = current_list2_node.next_element()
    return False

end_node = SingleLinkedNode.new(data=5, next_element=None)
third_node = SingleLinkedNode(data=3, next_element=None)
second_node = SingleLinkedNode.new(data=2, next_element=third_node)
first_node = SingleLinkedNode.new(data=1, next_element=second_node)
l1 = SingleLinkedList.new()
l2 = SingleLinkedList.new()
l1.append_node(first_node)
l1.append_node(second_node)
l1.append_node(third_node)
l2.append_node(end_node)
l2.append_node(first_node)
assert intersection(l1, l2)

