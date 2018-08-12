"""

LINKED LISTS - QUESTION 4
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
less than x. The partition element x can appear anywhere in the "right partition". It does not need to appear
between the left and right partitions.

Note that x does not have to be contained within the list.
Example input: 3 --> 5 --> 8 --> 5 --> 10 --> 2 --> 1 (partition = 5)
Example output: 3 --> 1 --> 2 --> 10 --> 5 --> 5 --> 8

"""
from single_linked_list import SingleLinkedList


def partition(linked_list, partition_data):
    new_linked_list = SingleLinkedList.new()
    current_node = linked_list.head()
    if not current_node:
        return None  # Should raise exception here, I just don't want to do unittest.
    while current_node is not None:
        if current_node.data() < partition_data:
            new_linked_list.insert_data_at_beggining(data=current_node.data())
        else:
            new_linked_list.append_data(data=current_node.data())
        current_node = current_node.next_element()
    return new_linked_list



# TEST 1
single_linked_list = SingleLinkedList.new()
single_linked_list.append_from_iterable(iterable=[1, 2, 3, 4, 1, 6, 7, 1])
single_linked_list.show()
new_list = partition(linked_list=single_linked_list, partition_data=6)
new_list.show()
new_list = partition(linked_list=single_linked_list, partition_data=4)
new_list.show()
new_list = partition(linked_list=single_linked_list, partition_data=2)
new_list.show()
new_list = partition(linked_list=single_linked_list, partition_data=7)
new_list.show()
new_list = partition(linked_list=single_linked_list, partition_data=5)
new_list.show()



