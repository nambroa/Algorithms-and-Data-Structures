"""

LINKED LISTS - QUESTION 1
Write code to remove duplicates from an unsorted linked list.

Note: I assume the intention is to remove duplicate DATA, not duplicate NODES (i.e objects).

QUESTIONS:

+ Can the list be empty? Yes
+ Can I recieve invalid input? Like a list with structs with no __eq__, or no list at all? No
+ Is the list single-linked or double-linked? Single-linked.

"""


def remove_duplicates_from(linked_list):
    if linked_list.length() == 0:
        return linked_list
    unique_nodes = set()
    current_node = linked_list.head()
    previous_node = None
    while current_node is not None:
        if current_node.data() in unique_nodes:
            # Delete the node from the linked list.
            # I have: previous node --> current node (to remove) --> next node
            # I need: previous node --> next node
            previous_node.set_next_element(current_node.next_element())
            if current_node == linked_list.tail():
                linked_list.set_tail(previous_node)
        else:
            unique_nodes.add(current_node.data())
            previous_node = current_node
        current_node = current_node.next_element()
    return linked_list
