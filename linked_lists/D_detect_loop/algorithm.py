"""

LINKED LISTS - QUESTION 8

Given a circular linked list, implement an algorithm that returns the node at the beggining of the loop.
DEF: A circular linked list is a corrupt linked list in which a node's next pointer points to an earlier
node, so as to make a loop in the linked list.

Example input: A --> B --> C --> D --> E --> C (the same C as earlier)
Output: C
Nodes can contain anything.

QUESTIONS:

+ Is the input valid? As in, a non-empty linked list with objs that can be compared with __eq__? Yes
 NOTE: since the list loops, you can't check it's length (its infinite).
+ Can the nodes be repeated in data (not at the object layer)? Yes
+ Will the list always contain a repeat? Yes

"""
from exercises.linked_lists.single_linked_list import SingleLinkedNode, SingleLinkedList


def detect_loop_in(linked_list):
    unique_nodes = set()
    current_node = linked_list.head()
    while current_node is not None:
        if current_node in unique_nodes:
            return current_node
        else:
            # If the node is too big and can't be stored, you can store only it's id by doing id(current_node).
            unique_nodes.add(current_node)
            current_node = current_node.next_element()

# TEST
first_node = SingleLinkedNode.new(data=1, next_element=None)
looped_node = SingleLinkedNode.new(data=5, next_element=first_node)
l1 = SingleLinkedList.new()
l1.append_node(first_node)
l1.append_node(looped_node)
assert detect_loop_in(l1) == first_node
l2 = SingleLinkedList.new()
l2.append_from_iterable([1, 2, 3])
assert not detect_loop_in(l2)
l3 = SingleLinkedList.new()
assert not detect_loop_in(l3)