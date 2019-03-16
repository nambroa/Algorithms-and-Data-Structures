"""

TREES AND GRAPHS - QUESTION 5

Implement a function to check if a binary tree is a BST (Binary Search Tree)

QUESTIONS YOU SHOULD ASK:

+ Can the tree contain duplicates? Yes (otherwise you can do In-Order Traversal and copy to an array, then see if it's sorted).
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""


# A BST is a binary tree that, for every node n, left children <= n < right_children
# Given an example Binary Tree that IS NOT a BST (Tree A):

#                 0
#              /     \
#            -6        6
#           /         / \
#         -8         4   8

# Now, let's see a valid BST (BST A):

#                 5
#              /     \
#             3        9
#           /  \      / \
#          2    4    8   10

# Let's also have a "mischievous" BST (Tree B). It would be like this:
#                 5
#              /     \
#             3        9
#           /  \      / \
#          2    6    8   10


# The main idea is to validate recursively.
# We know that the root has to be higher or equal than it's left child and lower than it's right child.
# However, the left child has to have a couple extra things for it to be considered a BST:
# 1) Its own left child must be smaller, no problem there.
# 2) Its own right child must be higher than him, BUT smaller than the root at the same time.
# We need to be able to remember the minimum and maximum allowed values for the children basically.
# So we will check recursively for the classic BST definition, while at the same time remembering this min/max boundary.

def validate_bst(root):
    return _validate_bst(root, None, None)


def _validate_left_branch(node, smaller_value):
    branch_validated = True
    if node.left_child() is not None:
        branch_validated &= node.data() >= node.left_child().data()
        if smaller_value is not None:
            branch_validated &= node.left_child().data() > smaller_value
    return branch_validated


def _validate_right_branch(node, bigger_value):
    branch_validated = True
    if node.right_child() is not None:
        branch_validated &= node.data() < node.right_child().data()
        if bigger_value is not None:
            branch_validated &= node.right_child().data() <= bigger_value
    return branch_validated


def _validate_bst(node, smaller_value, bigger_value):
    if node is None:
        return True
    left_branch_validated = _validate_left_branch(node, smaller_value)
    right_branch_validated = _validate_right_branch(node, bigger_value)
    if not left_branch_validated or not right_branch_validated:
        return False
    return _validate_bst(node.left_child(), None, node.data()) and _validate_bst(node.right_child(), node.data(), None)
