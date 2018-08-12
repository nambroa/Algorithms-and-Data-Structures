"""

LINKED LISTS - QUESTION 3
Implement an algorithm to delete a node in a single linked list, given ONLY access to that node.
That means you can't access the head or tail attributes of the list, and you will only recieve that node as input.
The node will never be the first or last node of the linked list.

"""

# I have: previous node --> current node (TO DELETE) --> next node
# I want previous node --> next node
# Since I can't access previous node, I will transform current node in next node, simulating the deletion.


def delete_middle_node_of(node):
    if node is None:
        raise ValueError("Invalid node (is None).")
    # Since the node is not the head or the tail, there always be a next element.
    next_element = node.next_element()
    node.set_data(next_element.data())
    node.set_next_element(next_element.next_element())
