"""

CTCI - TREES AND GRAPHS: QUESTION 8

Design an algorithm and write code to find the first common ancestor (FCA) of two nodes in a binary tree. Avoid storing
additional nodes in a data structure. NOTE: This is not necessarily a BST

EXAMPLE QUESTIONS TO ASK:

+ Can one of the nodes be invalid? Like None or empty? No
+ Can the tree contain repeated values? Yes, use their object ids to identify the ancestors.
+ What is a common ancestor? A parent that they have in common. In example Tree A, 4 and 8 have parent 6 as a
                             first common ancestor. Another ancestor would be 0 (but not the first common one!).
+ Will the two given nodes always have a first common ancestor? No, they may not have it.

"""

# Given an example Binary Tree (Tree A):

#                 0
#              /     \
#            -6        6
#           /         / \
#         -8         4   8

# Another longer one to better understand first common ancestor (Tree B). Think about the FCA of Node 11 and Node 12.
# How would you get it?

#                 0
#              /     \
#            -6        6
#           /         / \
#         -8         4   8
#                   / \   \
#                  5  10   12
#                       \
#                        11

# The first thing we will need is the depth of Node 1 and Node 2. Lets call them P1 and P2.
# One can be higher or equal than the other, so let's divide them into PMAX and PMIN.
# First, we raise the deeper node to the shallower node (in terms of height in the tree).
# This will allow us to raise both nodes in the tree at the same time, looking for their parents at the same speed.
# By doing this, we can be sure to find a first common ancestor if it exists.
# We also make sure that if some node reaches the root, then there is no common ancestor
# (since we started the search at the same depth for both nodes)

# This implementation is O(D), where D is the biggest depth (node1 or node2).


def get_depth_of(node1):
    current_depth = 0
    while node1 is not None:
        current_depth += 1
        node1 = node1.parent()
    return current_depth-1  # Because the current node1 (None) would be 1 space above the root.


def _identify_deeper_and_shallower_node(node1, node2):
    depth1, depth2 = get_depth_of(node1), get_depth_of(node2)
    if depth1 >= depth2:
        return depth1, depth2, node1, node2
    else:
        return depth2, depth1, node2, node1


def _go_up_to_the_shallower_node_depth(deeper_depth, shallower_depth, deeper_node):
    while deeper_depth != shallower_depth:
        deeper_node = deeper_node.parent()
        deeper_depth -= 1
    return deeper_node


def get_first_common_ancestor_between(node1, node2):
    deeper_depth, shallower_depth, deeper_node, shallower_node = _identify_deeper_and_shallower_node(node1, node2)
    heightened_node = _go_up_to_the_shallower_node_depth(deeper_depth, shallower_depth, deeper_node)
    while shallower_node is not None and heightened_node is not None:
        if shallower_node == heightened_node:
            return shallower_node
        shallower_node = shallower_node.parent()
        heightened_node = heightened_node.parent()
    return None

















