# Implement stack with a method that returns min.
# push, pop, and min must perform in O(1)

class myStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        print(value)
        self.stack.append(value)
        if len(self.min) == 0 or self.min[-1] >= value:
            self.min.append(value)

    def pop(self):
        if self.is_empty():
            return None
        elif self.min[-1] == self.stack[-1]:
                self.min.pop()
        return self.stack.pop()

    def get_min(self):
        if len(self.min) > 0:
            return self.min[-1]
        else:
            return "None"

    def is_empty(self):
        return len(self.stack) <= 0

from random import randint

s1 = myStack()
l = [randint(0, 9) for _ in range(5)]
print(l)
print(l)
for val in l:
    s1.push(val)

print(s1.get_min())
for val in l:
    s1.pop()
    print("new min: ", s1.get_min())

