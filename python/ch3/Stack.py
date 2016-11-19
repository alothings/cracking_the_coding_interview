
class Stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        # print(value)
        self.stack.append(value)
        # if len(self.min) == 0 or self.min[-1] >= value:
        #     self.min.append(value)

    def pop(self):
        if self.is_empty():
            return None
        # elif self.min[-1] == self.stack[-1]:
        #         self.min.pop()
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_min(self):
        if len(self.min) > 0:
            return self.min[-1]
        else:
            return "None"

    def is_empty(self):
        return len(self.stack) <= 0


