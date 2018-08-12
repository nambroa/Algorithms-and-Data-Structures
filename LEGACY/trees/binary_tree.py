# from django.core.exceptions import ValidationError


class BinaryTreeNode(object):
    def __init__(self, data, left_child=None, right_child=None, parent=None):
        self._data = data
        self._left_child = left_child
        self._right_child = right_child
        self._parent = parent

    @classmethod
    def new(cls, data, left_child=None, right_child=None, parent=None):
        tree_node = cls(data, left_child, right_child, parent)
        return tree_node

    def data(self):
        return self._data

    def left_child(self):
        return self._left_child

    def right_child(self):
        return self._right_child

    def parent(self):
        return self._parent

    def set_left_child(self, node):
        self._left_child = node
        node.set_parent(self)

    def set_right_child(self, node):
        self._right_child = node
        node.set_parent(self)

    def set_parent(self, node):
        self._parent = node

    def set_data(self, data):
        self._data = data

    def show(self):
        print(str(self.data()))
        if self.left_child():
            print("Left Child of {}:".format(str(self.data()))),
            self.left_child().show()
        if self.right_child():
            print("Right Child of {}:".format(str(self.data()))),
            self.right_child().show()


    def __str__(self):
        return str(self.data())


class BinaryTree(object):
    def __init__(self, root):
        self._root = root

    @classmethod
    def new(cls, root):
        tree = cls(root)
        return tree

    def root(self):
        return self._root

    def visit(self, node):
        print(str(node.data()))

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left_child())
            self.visit(node)
            self.in_order_traversal(node.right_child())

    def pre_order_traversal(self, node):
        if node is not None:
            self.visit(node)
            self.pre_order_traversal(node.left_child())
            self.pre_order_traversal(node.right_child())

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left_child())
            self.post_order_traversal(node.right_child())
            self.visit(node)


