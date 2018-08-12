class DoubleLinkedNode(object):
    def __init__(self, data, next_element, previous_element, **kwargs):
        self._data = data
        self._next_element = next_element
        self._previous_element = previous_element

    @classmethod
    def new(cls, data, next_element, previous_element):
        node = cls(data=data, next_element=next_element, previous_element=previous_element)
        return node

    def data(self):
        return self._data

    def next_element(self):
        return self._next_element

    def previous_element(self):
        return self._previous_element

    def set_previous_element(self, previous_element):
        self._previous_element = previous_element

    def set_next_element(self, next_element):
        self._next_element = next_element

    def set_data(self, data):
        self._data = data


class DoubleLinkedList(object):
    def __init__(self, **kwargs):
        self._head = None
        self._tail = None

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
        double_linked_list = cls()
        return double_linked_list

    def append(self, data):
        # Append new node to end of the list
        new_node = DoubleLinkedNode.new(data=data, next_element=None, previous_element=None)
        if self.tail():
            # It means list is not empty
            last_node = self.tail()
            last_node.set_next_element(next_element=new_node)
            new_node.set_previous_element(previous_element=last_node)
        else:
            # List is empty.
            self.set_head(head=new_node)
        self.set_tail(tail=new_node)

    def append_from_iterable(self, iterable):
        for elem in iterable:
            self.append(data=elem)

    def show(self):
        # Format is, for a list: [previous_node <-- current_node --> next_node]
        #                        [current_node <-- next_node --> next_of_next_node] ..
        if not self.head():
            print("EMPTY LIST")
            return
        current_node = self.head()
        while current_node is not None:
            print('['),
            if current_node.previous_element():
                print(current_node.previous_element().data()),
            else:
                print('None'),
            print('<--'),
            print(current_node.data()),
            print('-->'),
            if current_node.next_element():
                print(current_node.next_element().data()),
            else:
                print('None'),
            print(']')
            current_node = current_node.next_element()
        print('END')

# linked_list = DoubleLinkedList.new()
# linked_list.append_from_iterable(iterable=[1, 2, 3, 4, 1, 6, 7, 1])
# linked_list.show()
