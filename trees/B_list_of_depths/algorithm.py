"""

TREES AND GRAPHS - QUESTION 3

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
For example, if you have a tree with depth D, you'll have D linked lists.

QUESTIONS YOU SHOULD ASK:

+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes
+ Is the tree special in some way? Binary search? No, it can be anything really.
+ Can I use additional memory? Yes (you need the array of linked lists).

"""

# Given an example Binary Tree:
#                 0
#              /     \
#            -6        6
#           / \       / \
#         -8   -4    4   8
#               \
#                -2

# I can precompute a list of D empty linked lists. Then, I use DFS and remember the current depth, to add a node to the
# appropiate linked list.

from linked_lists.single_linked_list import SingleLinkedList


def list_of_depths(binary_tree):
    _validate_input(binary_tree)
    return _get_list_of_depths(binary_tree.root(), [], 0)


def _get_list_of_depths(tree_node, linked_lists, current_depth):
    if tree_node is None:
        return linked_lists
    linked_list = _get_linked_list(current_depth, linked_lists)
    linked_list.append_data(data=tree_node)
    _get_list_of_depths(tree_node.left_child(), linked_lists, current_depth + 1)
    _get_list_of_depths(tree_node.right_child(), linked_lists, current_depth + 1)
    return linked_lists


def _get_linked_list(current_depth, linked_lists):
    try:
        linked_list = linked_lists[current_depth]
    except IndexError:
        linked_list = SingleLinkedList.new()
        linked_lists.append(linked_list)
    return linked_list


def _validate_input(binary_tree):
    if binary_tree is None or binary_tree.root() is None:
        raise ValueError("Invalid Binary Tree.")
