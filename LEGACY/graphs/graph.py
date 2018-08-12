from resources.queues.queue import Queue


class GraphNode(object):
    def __init__(self, data, adyacents=None):
        self._data = data
        self._visited = False
        if not adyacents:
            self._adyacents = []
        else:
            self._adyacents = adyacents

    def data(self):
        return self._data

    def adyacents(self):
        return self._adyacents

    def visited(self):
        return self._visited

    def set_visited(self):
        self._visited = True

    def set_adyacents(self, adyacents):
        self._adyacents = adyacents

    def visit(self):
        print(str(self.data()))
        self._visited = True


# TODO: Add a map to access an individual node more easily. Check build_order exercise
class Graph(object):
    def __init__(self):
        self.nodes = []

    def visit(self, node):
        print(str(node.data()))

    def insert_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def depth_first_search(self, root):
        if root is None:
            return
        root.visit()
        adyacents = root.adyacents()
        for node in adyacents:
            if not node.visited():
                self.depth_first_search(root=node)

    def breadth_first_search(self, root):
        queue = Queue.new()
        if root is None:
            return
        queue.insert(root)
        while not queue.is_empty():
            current_node = queue.pop()
            current_node.visit()
            adyacents = current_node.adyacents()
            for node in adyacents:
                if not node.visited():
                    node.set_visited()
                    queue.insert(node)

