"""

TREES AND GRAPHS - QUESTION 2

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a BST with
minimal height.

QUESTIONS YOU SHOULD ASK:

+ Can I use custom classes? Yes.
+ Will the input always be valid? It can be a valid array or None
+ Are the integers positive? They can be anything, positive negative or zero.

"""

# So, given [-4,-2,0,3,5] I need to create a BST with minimal height. A BST is a Binary Tree with the
# following property: For every node with value n, left children <= n < right children.
# For minimal height, we need to aim to have a complete BST (or as close to it as possible)

# The trick is to think of "binary search, but with a tree". We want the root to be the middle number of the array
# Since this allows the smallest number of mandatory children (and reduces the height of the BST). With the same logic,
# I want the left children of the root to be the "middle node" of the first half of the array, and the right with
# the other half. We do this recursively until we have the tree.

# An example would be something like this:
# [-8,-6,-4,-2,0,2,4,6,8]
#                 0
#              /     \
#            -6        6
#           / \       / \
#         -8   -4    4   8
#               \
#                -2
from trees.binary_tree import BinaryTreeNode


def create_minimal_bst(numbers):
    _validate_input(numbers)
    if len(numbers) == 1:
        return BinaryTreeNode.new(data=numbers[0])
    return _recursive_create_minimal_bst(numbers, 0, len(numbers) - 1)


def _validate_input(numbers):
    if numbers is None:
        raise ValueError("The list needed to form the BST is None.")


def _recursive_create_minimal_bst(numbers, start, end):
    mid = int((start + end) / 2)
    node = BinaryTreeNode.new(data=numbers[mid])
    if 0 <= mid-1:
        node.set_left_child(node=_recursive_create_minimal_bst(numbers, 0, mid-1))
    if mid+1 <= end:
        node.set_right_child(node=_recursive_create_minimal_bst(numbers, mid+1, end))
    return node
