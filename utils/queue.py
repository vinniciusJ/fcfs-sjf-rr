class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def sort(self):
        self.queue.sort()

    def front(self):
        return self.queue[0]

    def __str__(self):
        separator = ' -> '

        return separator.join(map(str, self.queue))