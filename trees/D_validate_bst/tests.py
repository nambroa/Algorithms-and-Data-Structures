from unittest import TestCase

from trees.D_validate_bst.algorithm import validate_bst
from trees.binary_tree import BinaryTreeNode


class ValidateBSTTest(TestCase):
    def test_validate_bst_returns_true_for_a_valid_bst(self):
        root = self._make_valid_bst()
        self.assertTrue(validate_bst(root=root))

    def test_validate_bst_returns_false_for_an_invalid_bst(self):
        root = self._make_invalid_bst()
        self.assertFalse(validate_bst(root=root))

    def _make_valid_bst(self):
        node1 = BinaryTreeNode.new(data=5)
        node2 = BinaryTreeNode.new(data=3, parent=node1)
        node3 = BinaryTreeNode.new(data=9, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        node4 = BinaryTreeNode.new(data=2, parent=node2)
        node5 = BinaryTreeNode.new(data=4, parent=node2)
        node2.set_left_child(node4)
        node2.set_right_child(node5)
        node6 = BinaryTreeNode.new(data=8, parent=node2)
        node7 = BinaryTreeNode.new(data=10, parent=node2)
        node3.set_left_child(node6)
        node3.set_right_child(node7)
        return node1

    def _make_invalid_bst(self):
        node1 = BinaryTreeNode.new(data=5)
        node2 = BinaryTreeNode.new(data=3, parent=node1)
        node3 = BinaryTreeNode.new(data=9, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        node4 = BinaryTreeNode.new(data=2, parent=node2)
        node5 = BinaryTreeNode.new(data=6, parent=node2)
        node2.set_left_child(node4)
        node2.set_right_child(node5)
        node6 = BinaryTreeNode.new(data=8, parent=node2)
        node7 = BinaryTreeNode.new(data=10, parent=node2)
        node3.set_left_child(node6)
        node3.set_right_child(node7)
        return node1
