"""

TREES AND GRAPHS - QUESTION 4

Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree
is defined to be a tree such that the heights of two subtrees of any node never differ by more than one.

QUESTIONS YOU SHOULD ASK:

+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes
+ Is the binary tree a BST? No
+ Can the tree be empty? Yes, in this case we'll say it is balanced.

"""


# It seems to be a recursive question. I need a way to iterate over the tree, like DFS. I keep a counter for the current
# tree depth. Each time I go lower, I increase that depth count.
# Base case would be if the node is None, in which case I returned the stored height minus 1.
# For a node, I need to recursively call the same function for their left and right child.
# If I see that the current subtrees are not balanced, I raise an exception and return False.
# Otherwise, just return True.

# Given an example Binary Tree:
#                 0
#              /     \
#            -6        6
#           / \       / \
#         -8   -4    4   8
#               \
#                -2

class BinaryTreeNotBalancedException(Exception):
    pass


def check_if_binary_tree_is_balanced(binary_tree):
    if binary_tree.root() is None:
        return True
    try:
        _check_balanced(binary_tree.root(), 0)
        return True
    except BinaryTreeNotBalancedException:
        return False


def _check_balanced(node, current_depth):
    if node is None:
        return current_depth - 1
    left_height = _check_balanced(node.left_child(), current_depth + 1)
    right_height = _check_balanced(node.right_child(), current_depth + 1)
    if abs(left_height - right_height) > 1:
        raise BinaryTreeNotBalancedException()
    return max(left_height, right_height)
