# Stack is a LIFO structure


class Stack(object):

    def __init__(self):
        self.items = []

    @classmethod
    def new(cls):
        stack = cls()
        return stack

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise ValueError("EMPTY STACK")
        return self.items.pop()

    def peek(self):
        items_length = len(self.items)
        return self.items[items_length-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        # I can do this since self.items is an array.
        # Otherwise, I would need to keep a counter and add/substract to it in each push/pop.
        return len(self.items)

    def show(self):
        if self.is_empty():
            return "EMPTY STACK"
        i = len(self.items) - 1
        while i >= 0:
            elem = self.items[i]
            print(str(elem))
            i -= 1
        print("---------")


# stack = Stack.new()
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.show()
# stack.pop()
# stack.show()
# stack.pop()
# stack.show()
