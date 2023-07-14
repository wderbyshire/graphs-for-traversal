class ListQueue:
    def __init__(self):
        self.list_queue = []

    def enqueue(self, value):
        self.list_queue.insert(0, value)

    def dequeue(self):
        if self.list_queue:
            self.list_queue.pop(0)
        else:
            raise IndexError("Queue has no values to dequeue")

    def size(self):
        return len(self.list_queue)

    def __str__(self):
        return str(self.list_queue)