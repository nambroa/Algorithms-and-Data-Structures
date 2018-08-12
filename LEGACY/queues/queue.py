# Queue is a FIFO structure.
from collections import deque


class Queue(object):

    def __init__(self):
        self.items = deque()

    @classmethod
    def new(cls):
        queue = cls()
        return queue

    def insert(self, data):
        self.items.appendleft(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        try:
            is_not_empty = self.items[0]
            return False
        except IndexError:
            return True

    def show(self):
        if self.is_empty():
            return "EMPTY QUEUE"
        for elem in self.items:
            print(str(elem))
        print("---------")

q = Queue.new()
q.show()
q.insert(3)
q.show()
q.insert(2)
q.show()
q.insert(1)
q.show()
q.pop()
q.show()
print(str(q.is_empty()))
q.pop()
q.pop()
print(str(q.is_empty()))