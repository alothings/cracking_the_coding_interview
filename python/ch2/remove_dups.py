from LinkedList import LinkedList, Node

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    hash_set = set([current.value])
    while current.next:
        if current.next.value in hash_set:
            current.next = current.next.next
        else:
            hash_set.add(current.next.value)
            current = current.next
    return ll

ll = LinkedList()
ll.generate(20, 0, 9)
print(ll)
remove_dups(ll)
print("Result: ", ll)



