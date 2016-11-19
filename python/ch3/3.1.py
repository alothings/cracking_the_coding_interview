# 3 stacks in an array

class ThreeStacks(object):
    def __init__(self, size):
        self.size = size
        self.stack_list = [None for _ in range(3*size)]
        self.pointer = [0*size, 1*size, 2*size]

    def __str__(self):
        values = [str(x) for x in self.stack_list]
        return ' -> '.join(values)

    def push(self, stack_index, data):
        if 2 < stack_index < 0:
            raise Exception("Error!")
        elif self.pointer[stack_index] == self.size*stack_index + self.size:
            raise Exception("Stack Full")
        else:
            self.stack_list[self.pointer[stack_index]] = data
            self.pointer[stack_index] += 1

    def pop(self, stack_index):
        temp = self.stack_list[self.pointer[stack_index]]
        self.stack_list[self.pointer[stack_index]] = None
        self.pointer[stack_index] -= 1
        return temp

if __name__ == "__main__":
    myStack = ThreeStacks(100)
    for i in range(10):
        myStack.push(0, i)
    print(myStack)
    for i in range(11):
        print(myStack.pop(0))
    print(myStack)




