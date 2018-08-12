"""

TREES AND GRAPHS - QUESTION 3

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
For example, if you have a tree with depth D, you'll have D linked lists.

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes

"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from resources.linked_lists.single_linked_list import SingleLinkedList
from resources.queues.queue import Queue
from resources.trees.binary_tree import BinaryTreeNode, BinaryTree

"""

First solution.

"""

def list_of_depths(root):
    if not root: raise ValidationError("No root node detected")
    return get_list_of_depths(root, 0, [])


def get_list_of_depths(node, depth, linked_lists):
    if not node: return linked_lists
    try:
        linked_list = linked_lists[depth]
        linked_list.append_data(node)
    except IndexError:
        linked_list = SingleLinkedList.new()
        linked_list.append_data(node)
        linked_lists.append(linked_list)
    get_list_of_depths(node.left_child(), depth+1, linked_lists)
    get_list_of_depths(node.right_child(), depth+1, linked_lists)
    return linked_lists

"""

Another solution, using BFS.

"""


def bfs_list_of_depths(tree_node, linked_lists):
    queue = Queue.new()
    queue.insert((tree_node, 0))
    while not queue.is_empty():
        node, depth = queue.pop()
        try:
            linked_list = linked_lists[depth]
            linked_list.append_data(node)
        except IndexError:
            linked_list = SingleLinkedList.new()
            linked_list.append_data(node)
            linked_lists.append(linked_list)
        if node.left_child():
            queue.insert((node.left_child(), depth+1))
        if node.right_child():
            queue.insert((node.right_child(), depth+1))
    return linked_lists


class ListOfDepthsTest(TestCase):
    def test_list_of_depths_raises_exception_when_nothing_is_passed_to_it(self):
        self.assertRaises(ValidationError, list_of_depths, None)

    def test_list_of_depths_returns_hashmap_of_2_linked_lists_for_a_tree_with_2_depth_levels(self):
        node1 = BinaryTreeNode.new(data=1)
        node2 = BinaryTreeNode.new(data=2, parent=node1)
        node3 = BinaryTreeNode.new(data=3, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        tree = BinaryTree.new(root=node1)
        linked_lists_hashmap = list_of_depths(root=tree.root())
        self.assertTrue(linked_lists_hashmap[0])
        self.assertTrue(linked_lists_hashmap[1])
        self.assertEqual(linked_lists_hashmap[0].head().data(), node1)
        self.assertEqual(linked_lists_hashmap[1].head().data(), node2)
        self.assertEqual(linked_lists_hashmap[1].tail().data(), node3)

    def test_list_of_depths_returns_hashmap_of_3_linked_lists_for_a_tree_with_3_depth_levels(self):
        node1 = BinaryTreeNode.new(data=1)
        node2 = BinaryTreeNode.new(data=2, parent=node1)
        node3 = BinaryTreeNode.new(data=3, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        node4 = BinaryTreeNode.new(data=4, parent=node2)
        node2.set_left_child(node4)
        tree = BinaryTree.new(root=node1)
        linked_lists_hashmap = list_of_depths(root=tree.root())
        self.assertTrue(linked_lists_hashmap[0])
        self.assertTrue(linked_lists_hashmap[1])
        self.assertTrue(linked_lists_hashmap[2])
        self.assertEqual(linked_lists_hashmap[0].head().data(), node1)
        self.assertEqual(linked_lists_hashmap[1].head().data(), node2)
        self.assertEqual(linked_lists_hashmap[1].tail().data(), node3)
        self.assertEqual(linked_lists_hashmap[2].head().data(), node4)
