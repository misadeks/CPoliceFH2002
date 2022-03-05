from collections import deque


class Stack:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def __int__(self):
        return len(self.data)

    def __bool__(self):
        return len(self.data) != 0

    def empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1]

    def take(self):
        value = self.data[-1]
        self.data.pop()
        return value
