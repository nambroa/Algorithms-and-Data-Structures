"""

TREES AND GRAPHS - QUESTION 6

Write an algorithm to find the "next" node (i.e in-order successor) of a given node in a BST. You may assume that
each node has a link to its parent.

QUESTIONS YOU SHOULD ASK:

+ Can the tree contain duplicates? No
+ Can the tree be None or empty? No
+ Do I need to validate that the given tree is a BST? No, you can assume it will always be a BST.
+ Will the given node always have a successor? Yes

"""


# Given a valid BST (BST A):

#                 5
#              /     \
#             3        7
#           /  \      / \
#          2    4    6   14
#                        /
#                      12
# The in order order would be: [2, 3, 4, 5, 8, 9, 10]

# If you are just given the node, you can't start at the root. let's say you were given the node 5, which next node
# is 6. Basically, since 5 has a right subtree, we know that the next one will be at the leftmost part of the right
# subtree.

# Now let's say you don't have a right subtree. Let's say you were given the node 4. This means that your next node
# is one of your parents. However, how do you know if 3 or 5 is the correct answer? Basically, you need to keep
# moving up until you find a node that is bigger than you, and that is the correct answer.

# It is key to remember that the tree does not contain duplicates.

def _get_leftmost_leaf_of_(node):
    left_child = node.left_child()
    if left_child is None:
        return node
    else:
        previous_node = None
        while left_child is not None:
            previous_node = left_child
            left_child = left_child.left_child()
        return previous_node


def in_order_successor_of(node):
    if node.right_child() is not None:
        return _get_leftmost_leaf_of_(node.right_child())
    else:
        parent = node.parent()
        while parent is not None:
            if parent.data() > node.data():
                return parent
            else:
                parent = parent.parent()
