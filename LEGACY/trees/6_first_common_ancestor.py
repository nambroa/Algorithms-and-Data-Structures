"""

CTCI - TREES AND GRAPHS: QUESTION 8

Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing
additional nodes in a data structure. NOTE: This is not necessarily a BST


"""

"""

First, a naive implementation that stores additional data in a set.
Complexity: O(n). In the worst case, I iterate over every node on the tree. On each iteration, I perform O(1) operations
since the "in" operation is O(1) in a set, and the add is also O(1).

NOTA DE NICO: Me parece que la complejidad es O(H) Con H la altura del arbol!

This assumes that node1 and node2 come from the same tree, such that they will always have a first_common_ancestor.
It's easy to refactor it so that it allows nodes from different trees though.

"""


def first_common_ancestor(tree, node1, node2):
    if not tree or not node1 or not node2: raise ValueError("Invalid function parameters")
    empty_set = set()
    return rec_first_common_ancestor(tree, node1, node2, empty_set)


def rec_first_common_ancestor(tree, node1, node2, visited_nodes):
    if node1.parent() == tree.root() and node2.parent() == tree.root(): return tree.root()
    if node1.parent() == tree.root() and node2.parent() != tree.root():
        return rec_first_common_ancestor(tree, node1, node2.parent(), visited_nodes)
    if node1.parent() != tree.root() and node2.parent() == tree.root():
        return rec_first_common_ancestor(tree, node1.parent(), node2, visited_nodes)
    if id(node1) in visited_nodes: return node1
    if id(node2) in visited_nodes: return node2
    visited_nodes.add(id(node1))
    visited_nodes.add(id(node2))
    rec_first_common_ancestor(tree, node1.parent(), node2.parent(), visited_nodes)


"""

Secondly, a better implementation that takes O(D), where D is the biggest depth(node1 or node2).

"""


def better_first_common_ancestor(node1, node2):
    delta_depth = depth(node1) - depth(node2)
    deeper_node = node1 if delta_depth > 0 else node2
    shallower_node = node2 if delta_depth > 0 else node1
    # Move the deeper node up to the depth of the shallower node.
    deeper_node = go_up(shallower_node, abs(delta_depth))
    # See where the paths intersect.
    while deeper_node != shallower_node and deeper_node is not None and shallower_node is not None:
        deeper_node = deeper_node.parent()
        shallower_node = shallower_node.parent()

    if deeper_node is None or shallower_node is None: return None  # No common ancestor
    return deeper_node


def go_up(node, delta):
    while delta > 0:
        node = node.parent()
        delta -= 1
    return node


def depth(node):
    res = 0
    while node is not None:
        res += 1
        node = node.parent()
    return res