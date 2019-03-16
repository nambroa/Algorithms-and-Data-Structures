from unittest import TestCase

from trees.E_successor.algorithm import in_order_successor_of
from trees.binary_tree import BinaryTreeNode


class InOrderSuccessorTest(TestCase):
    def test_in_order_successor(self):
        node1 = BinaryTreeNode.new(data=3)
        node2 = BinaryTreeNode.new(data=1, parent=node1)
        node3 = BinaryTreeNode.new(data=4, parent=node1)
        node1.set_left_child(node2)
        node1.set_right_child(node3)
        node4 = BinaryTreeNode.new(data=0, parent=node2)
        node5 = BinaryTreeNode.new(data=2, parent=node2)
        node2.set_left_child(node4)
        node2.set_right_child(node5)
        self.assertEqual(in_order_successor_of(node5), node1)
