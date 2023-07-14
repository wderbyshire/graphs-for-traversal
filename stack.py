class ListStack:
    def __init__(self):
        self.list_stack = []

    def push(self, value):
        self.list_stack.append(value)

    def pop(self):
        if self.list_stack:
            return self.list_stack.pop()
        else:
            raise IndexError("Stack has no values to pop")

    def size(self):
        return len(self.list_stack)

    def __str__(self):
        return str(self.list_stack)
