# Find kth element from the end in a Linked List

from LinkedList import LinkedList

def find_kth(head, k):
    current = runner = head
    for i in range(0, k):
        # print("i ", i)
        if runner is None: return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current.value

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
print(ll)
print(find_kth(ll.head, 1))
print(find_kth(ll.head, 2))
print(find_kth(ll.head, 3))
print(find_kth(ll.head, 4))
print(find_kth(ll.head, 5))
print(find_kth(ll.head, 6))
