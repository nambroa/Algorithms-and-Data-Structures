"""

TREES AND GRAPHS - QUESTION 2

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a BST with
minimal height.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""
from resources.trees.binary_tree import BinaryTreeNode


def minimal_bst(array_of_ints):
    return create_minimal_bst_recursive(array_of_ints, 0, len(array_of_ints)-1)


def create_minimal_bst_recursive(ints, start, end):
    if start <= end:
        mid = (start + end) / 2
        node = BinaryTreeNode.new(data=ints[mid])
        node.set_left_child(node=create_minimal_bst_recursive(ints, start, mid-1))
        node.set_right_child(node=create_minimal_bst_recursive(ints, mid+1, end))
        return node
    return BinaryTreeNode.new(data=None)