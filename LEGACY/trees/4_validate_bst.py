"""

TREES AND GRAPHS - QUESTION 5

Implement a function to check if a binary tree is a BST (Binary Search Tree)

QUESTIONS YOU SHOULD ASK:
+ Can the tree contain duplicates? Yes (otherwise you can do In-Order Traversal and copy to an array, then see if it's sorted).
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""


def validate_bst(node, min, max):
    if not node:
        return True

    if (min and node.data() <= min) or (max and node.data() > max):
        return False

    if (not validate_bst(node.left_child(), min, node.data())) or (not validate_bst(node.right_child(), node.data()+1, max)):
        return False

    return True


def check_bst(root):
    return validate_bst(root, None, None)

