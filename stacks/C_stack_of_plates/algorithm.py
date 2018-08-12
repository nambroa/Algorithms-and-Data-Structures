"""

STACKS AND QUEUES - QUESTION 3

Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this.
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
Methods pop() and push() should behave as they do as a normal stack

QUESTIONS YOU SHOULD ASK:

+ Will I get the capacity via input? What type will it be? Yes, it will be an integer.
+ Can it be negative? If so, what should I return? Yes, return an exception.
+ Can it be zero? No

"""
from exercises.stacks.stack import Stack


class LimitedSizeStack(object):
    def __init__(self, size_limit):
        if size_limit <= 0:
            raise ValueError("Stack size limit needs to be positive.")
        self._size_limit = size_limit
        self._stack = Stack.new()

    def size_limit(self):
        return self._size_limit

    def push(self, elem):
        if self._stack.size() >= self.size_limit():
            raise ValueError("Stack size limit reached. Please pop some elements out first.")
        self._stack.push(elem)

    def peek(self):
        return self._stack.peek()

    def pop(self):
        self._stack.pop()

    def is_full(self):
        return self.size_limit() <= self._stack.size()


"""

I expect this object to behave like a normal stack, so you can't push or pop to or from a specific stack.
You can however check the size limit, since it is provided in creation.

"""


class SetOfStacks(object):
    def __init__(self, stack_size_limit):
        if stack_size_limit <= 0:
            raise ValueError("Stack size limit needs to be positive.")
        self._stack_size_limit = stack_size_limit
        self._stacks = []

    def stack_size_limit(self):
        return self._stack_size_limit

    def push(self, elem):
        if len(self._stacks) == 0:
            # Create first stack
            stack = LimitedSizeStack(size_limit=self.stack_size_limit())
            stack.push(elem)
            self._stacks.append(stack)
        else:
            # Push to current stack, or create one if it's full.
            current_stack = self._stacks[-1]
            if current_stack.is_full():
                new_stack = LimitedSizeStack(size_limit=self.stack_size_limit())
                new_stack.push(elem)
                self._stacks.append(new_stack)
            else:
                current_stack.push(elem)

    def pop(self):
        if len(self._stacks) == 0:
            raise ValueError("The stack is empty. Please push some elements first.")
        current_stack = self._stacks[-1]
        current_stack.pop()
        if len(current_stack) == 0:
            # Remove the stack, since it's empty.
            self._stacks.pop()


