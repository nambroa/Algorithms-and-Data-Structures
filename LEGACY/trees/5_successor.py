"""

TREES AND GRAPHS - QUESTION 6

Write an algorithm to find the "next" node (i.e in-order successor) of a given node in a BST. You may assume that
each node has a link to its parent

QUESTIONS YOU SHOULD ASK:
+ Can the tree contain duplicates? No
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""
from resources.trees.binary_tree import BinaryTreeNode


def leftmost_of(node):
    if node is None:
        return None
    while node.left_child():
        node = node.left_child()
    return node


def in_order_successor(node):
    if node is None:
        return None

    if node.right_child():
        # If the node has a right subtree, the successor will always be in the leftmost of it.
        return leftmost_of(node.right_child())
    else:
        current = node
        parent = node.parent()
        # Now we need to go up until we are on the the left instead of right subtree.
        while parent is not None and parent.left_child() != current:
            # If the node doesnt have a right subtree and is on the left subtree, then the successor is its parent.
            current = parent
            parent = current.parent()
        return parent


node1 = BinaryTreeNode.new(data=3)
node2 = BinaryTreeNode.new(data=1, parent=node1)
node3 = BinaryTreeNode.new(data=4, parent=node1)
node1.set_left_child(node2)
node1.set_right_child(node3)
node4 = BinaryTreeNode.new(data=0, parent=node2)
node5 = BinaryTreeNode.new(data=2, parent=node2)
node2.set_left_child(node4)
node2.set_right_child(node5)
assert in_order_successor(node5) == node1



