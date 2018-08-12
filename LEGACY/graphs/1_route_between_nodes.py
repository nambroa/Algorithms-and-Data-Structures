"""

CTCI - TREES AND GRAPHS - QUESTION 1

Given a directed graphm design an algorithm to find out whether there is a route between two nodes, node1 and node2

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes.
+ Will the input always be valid? Yes
+ Does the route need to be minimal? No

"""
from unittest import TestCase

from django.core.exceptions import ValidationError

from graphs.graph import GraphNode
from resources.queues.queue import Queue


def _validate_input(node1, node2):
    if not node1 or not node2:
        raise ValidationError("Invalid Input: missing nodes")


def route_between_nodes(node1, node2):
    # A modified BFS
    queue = Queue.new()
    _validate_input(node1, node2)
    if node1 is node2:
        return True
    queue.insert(node1)
    while not queue.is_empty():
        current_node = queue.pop()
        current_node.visit()
        adyacents = current_node.adyacents()
        for adyacent_node in adyacents:
            if adyacent_node == node2:
                return True
            if not adyacent_node.visited():
                adyacent_node.set_visited()
                queue.insert(adyacent_node)
    return False


class RouteBetweenNodesTest(TestCase):
    def test_route_between_connected_nodes_should_return_true(self):
        gnode1 = GraphNode(data=2)
        gnode2 = GraphNode(data=3, adyacents=[gnode1])
        self.assertTrue(route_between_nodes(node1=gnode2, node2=gnode1))

    def test_route_between_same_nodes_should_return_true(self):
        gnode1 = GraphNode(data=2)
        self.assertTrue(route_between_nodes(node1=gnode1, node2=gnode1))

    def test_route_between_unconnected_nodes_should_return_false(self):
        gnode1 = GraphNode(data=2)
        gnode2 = GraphNode(data=3)
        self.assertFalse(route_between_nodes(node1=gnode1, node2=gnode2))
