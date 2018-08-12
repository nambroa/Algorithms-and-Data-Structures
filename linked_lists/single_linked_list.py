class EmptyListException(Exception):
    pass


class SingleLinkedNode(object):
    def __init__(self, data, next_element, **kwargs):
        self._data = data
        self._next_element = next_element

    def __repr__(self):
        return str(self.data())

    @classmethod
    def new(cls, data, next_element):
        node = cls(data=data, next_element=next_element)
        return node

    def data(self):
        return self._data

    def next_element(self):
        return self._next_element

    def set_next_element(self, next_element):
        self._next_element = next_element

    def set_data(self, data):
        self._data = data


class SingleLinkedList(object):
    def __init__(self, **kwargs):
        self._head = None
        self._tail = None

    def __str__(self):
        return "Head: %s" % self.head()

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def set_tail(self, tail):
        self._tail = tail

    def set_head(self, head):
        self._head = head

    @classmethod
    def new(cls):
        linked_list = cls()
        return linked_list

    def length(self):
        current_node = self.head()
        if not current_node:
            return 0
        i = 0
        while current_node is not None:
            i += 1
            current_node = current_node.next_element()
        return i

    def append_data(self, data):
        new_node = SingleLinkedNode.new(data=data, next_element=None)
        self.append_node(new_node=new_node)

    def append_node(self, new_node):
        if self.tail():
            # It means list is not empty
            last_node = self.tail()
            last_node.set_next_element(next_element=new_node)
        else:
            # List is empty.
            self.set_head(head=new_node)
        self.set_tail(tail=new_node)

    def append_from_iterable(self, iterable):
        for elem in iterable:
            self.append_data(data=elem)

    def insert_data_at_beggining(self, data):
        new_node = SingleLinkedNode.new(data=data, next_element=None)
        self.insert_node_at_beggining(new_node=new_node)

    def insert_node_at_beggining(self, new_node):
        if self.head():
            # It means list is not empty
            first_node = self.head()
            new_node.set_next_element(next_element=first_node)
            self.set_head(head=new_node)
        else:
            # List is empty.
            self.set_head(head=new_node)
            self.set_tail(tail=new_node)

    def has_repeated_nodes(self):
        if self.length() == 0:
            return False
        unique_nodes = set()
        current_node = self.head()
        while current_node is not None:
            if current_node in unique_nodes:
                return True
            else:
                unique_nodes.add(current_node)
            current_node = current_node.next_element()
        return False

    def show(self):
        if not self.head():
            print("EMPTY LIST")
            return
        current_node = self.head()
        while current_node is not None:
            print(current_node.data()),
            print('-->'),
            current_node = current_node.next_element()
        print('END')
