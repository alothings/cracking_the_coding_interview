from LinkedList import LinkedList

def delete_middle_node(n):
    n.value = n.next.value
    n.next = n.next.next

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
middle_node = ll.add(5)
ll.add(6)
ll.add(7)

print(ll)
delete_middle_node(middle_node)
print(ll)