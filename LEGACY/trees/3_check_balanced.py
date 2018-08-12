"""

TREES AND GRAPHS - QUESTION 4

Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree
is defined to be a tree such that the heights of two subtrees of any node never differ by more than one.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""


def check_balanced(tree_node):
    if tree_node is not None:
        try:
            heights = check_balanced_recursive(tree_node)
            return True
        except ValueError:
            return False
    raise ValueError("Invalid input")


def check_balanced_recursive(tree_node):
    if tree_node is None:
        return -1
    left_height = check_balanced(tree_node.left_child())
    right_height = check_balanced(tree_node.right_child())
    diff = abs(left_height - right_height)
    if diff > 1: raise ValueError("Tree not Balanced")
    return max(left_height, right_height) + 1


"""

A nicer implementation below (only possible in dynamic languages like Python):

def check_balanced(root):
    return bool(recursive_check_balanced(root))

def recursive_check_balanced(node):
    if not node: return -1 # at the end
    left_subtree_length = recursive_check_balanced(node.left_child())
    right_subtree_length = recursive_check_balanced(node.right_child())
    if abs(left_subtree_length-right_subtree_length) > 1: return False
    return max(left_subtree_length, right_subtree_length)+1

"""
