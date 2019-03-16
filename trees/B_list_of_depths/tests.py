from unittest import TestCase

from trees.B_list_of_depths.algorithm import list_of_depths
from trees.binary_tree import BinaryTreeNode, BinaryTree


class ListOfDepthsTest(TestCase):
    def test_list_of_depths_raises_exception_when_nothing_is_passed_to_it(self):
        self.assertRaises(ValueError, list_of_depths, None)

    def test_list_of_depths_returns_hashmap_of_2_linked_lists_for_a_tree_with_2_depth_levels(self):
        node1 = BinaryTreeNode.new(data=1)
        node2 = BinaryTreeNode.new(data=2, parent=node1)
        node3 = BinaryTreeNode.new(data=3, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        tree = BinaryTree.new(root=node1)
        linked_lists_hashmap = list_of_depths(binary_tree=tree)
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
        linked_lists_hashmap = list_of_depths(binary_tree=tree)
        self.assertTrue(linked_lists_hashmap[0])
        self.assertTrue(linked_lists_hashmap[1])
        self.assertTrue(linked_lists_hashmap[2])
        self.assertEqual(linked_lists_hashmap[0].head().data(), node1)
        self.assertEqual(linked_lists_hashmap[1].head().data(), node2)
        self.assertEqual(linked_lists_hashmap[1].tail().data(), node3)
        self.assertEqual(linked_lists_hashmap[2].head().data(), node4)
