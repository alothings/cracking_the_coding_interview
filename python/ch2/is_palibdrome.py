#method to check if Linked List singly, is palidrome
from LinkedList import LinkedList

def is_palindrome(head):
    l = []
    current = head
    size = 0
    # Loop over linked list to get size, and append items to list
    while current:
        l.append(current.value)
        current = current.next
        size += 1
    # loop over half of the linked list to compare
    for i in range(int(size/2)):
        # print("head.val {}, l.pop {}".format(head.value, l[-1]))
        if head.value is not l.pop():
            return False
        head = head.next
    return True

ll = LinkedList()
ll.add_multiple([1, 2, 3, 2, 1])
print(ll)
print(is_palindrome(ll.head))

ll2 = LinkedList()
ll2.add_multiple([1,2,3,2,14])
print(ll2)
print(is_palindrome(ll2.head))
