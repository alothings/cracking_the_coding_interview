from Stack import Stack
from random import randint

def sort_stack(s):
    r = Stack()
    while not s.is_empty():
        tmp = s.pop()
        while not r.is_empty() and r.peek() > tmp:
            s.push(r.pop())
        r.push(tmp)

    #Putthing stuff back to initial stack
    while not r.is_empty():
        s.push(r.pop())


my_stack = Stack()
l = [randint(0, 9) for _ in range(10)]
# print("input: ", l)
for val in l:
    my_stack.push(val)

print("Initial: ", my_stack)
sort_stack(my_stack)
print("Solution: ", my_stack)