# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# For this exercise, we will be using DFS Inorder as our tree traversal method.


def get_list_of_depths(tree_node, list_of_depths, current_depth):
    if tree_node is not None:
        list_of_depths.append(current_depth)
        get_list_of_depths(tree_node.left, list_of_depths, current_depth+1)
        print("Visiting {0}".format(tree_node.val))
        print("Current Depth: {0}".format(current_depth))
        get_list_of_depths(tree_node.right, list_of_depths, current_depth+1)
    return max(list_of_depths)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return get_list_of_depths(root, [0], 1)