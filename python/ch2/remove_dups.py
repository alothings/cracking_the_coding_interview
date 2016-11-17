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

def remove_dups_runner(ll):
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if current.value is not runner.next.value:
                runner = runner.value
            else:
                runner.next = runner.next.next
    return ll


ll = LinkedList()
ll.generate(100, 0, 6)
print(ll)
remove_dups(ll)
print("Result: ", ll)

ll2 = LinkedList()
ll2.generate(100, 0, 6)
print(ll2)
remove_dups(ll2)
print("Result: ", ll2)



