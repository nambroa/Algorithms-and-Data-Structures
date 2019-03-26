"""

STACKS AND QUEUES - QUESTION 4

Implement a MyQueue class which implements a queue using two stacks.

QUESTIONS YOU SHOULD ASK:

+ What will the stacks contain? Numbers
+ Can I use custom classes? No, only MyQueue. The idea is to do the exercise with ONLY two normal stacks.

"""
from stacks.stack import Stack

"""

STACK --> LIFO --> El primero que entra es último en irse.
QUEUE --> FIFO --> El primero que entra es el primero que se va.

Por ejemplo. Llegan 1, 2, 3 en ese orden.
STACK pop --> [1, 2] --> STACK pop --> [1]
QUEUE dequeue --> [2, 3] --> QUEUE dequeue --> [2]

La idea es que si pusheo a Stack 1, y despues pusheo a Stack 2, me quedan como en la cola

Entonces, voy a tener un stack para los nuevos elementos y otro para los viejos. Cuando sea hora de eliminar, paso
las cosas al stack viejo y me quedan como en la cola. Push se va a hacer al stack 1 (el nuevo).

"""


class MyQueue(object):
    def __init__(self):
        self._newest_elements = Stack.new()
        self._oldest_elements = Stack.new()

    def push(self, elem):
        self._newest_elements.push(elem)

    def dequeue(self):
        if len(self._newest_elements) == 0 and len(self._oldest_elements) == 0:
            raise ValueError("Queue is empty. Please add some elements first.")
        if len(self._oldest_elements) == 0:
            while len(self._newest_elements) > 0:
                elem = self._newest_elements.pop()
                self._oldest_elements.push(elem)
        return self._oldest_elements.pop()
