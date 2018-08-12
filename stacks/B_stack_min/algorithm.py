"""

STACKS AND QUEUES - QUESTION 2

How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push pop and min should all operate in O(1).

QUESTIONS YOU SHOULD ASK:
+ Can I use custom classes? Yes
+ What can the stacks contain? Numbers. Can they be negative? Yes
+ Will the input always be valid? Yes

"""


class MinStack(object):
    def __init__(self):
        self._stack =[]
        self._mins = []

    def push(self, elem):
        self._stack.append(elem)
        if elem < self._mins[-1]:
            self._mins.append(elem)

    def pop(self):
        elem = self._stack[-1]
        if elem == self.min():
            self._mins.pop()
        self._stack.pop()

    def min(self):
        return self._mins[-1]