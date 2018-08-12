class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    @classmethod
    def new(cls, data):
        tree_node = cls(data)
        return tree_node


class Tree(object):
    def __init__(self, root):
        self.root = root

    @classmethod
    def new(cls, root):
        tree = cls(root)
        return tree