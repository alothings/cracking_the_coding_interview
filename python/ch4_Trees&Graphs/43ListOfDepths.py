
class NodeLL(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object): # queue behavior

    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = NodeLL(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = NodeLL(data)

    def remove(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def show(self):
        x = self.head
        while x is not None:
            print(x.data.key, "-> ", end='')
            x = x.next
        print(None)

class NodeBST(object):

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, root=None):
        self.root = root

    def put(self, key, val=None):
        self.root = self._put(key, val, self.root)
        return self.root

    def _put(self, key, val, x):
        if x is None:
            return NodeBST(key, val)
        if key < x.key:
            x.left = self._put(key, val, x.left)
        elif key > x.key:
            x.right = self._put(key, val, x.right)
        else:
            x.val = val
        return x

    def get(self, key):
        x = self._get(key, self.root)
        if x is None:
            return None
        else:
            return x.val

    def _get(self, key, x):
        if x is None:
            return None
        if key < x.key:
            return self._put(key, val, x.left)
        elif key > x.key:
            return self._put(key, val, x.right)
        else:
            return val


def create_level_lists(root):
    lists = []
    create_level_list(root, lists, 0)
    return lists


def create_level_list(root, lists, level):
    if root is None: return
    # list = []
    if len(lists) == level:
        list = []
        lists.append(list)
    else:
        list = lists[level]
    list.append(root)
    create_level_list(root.left, lists, level + 1)
    create_level_list(root.right, lists, level + 1)
    return lists

if __name__ == "__main__":
    bst = BST()
    bst.put(8)
    bst.put(4)
    bst.put(12)
    bst.put(2)
    bst.put(6)
    bst.put(10)
    bst.put(14)
    bst.put(1)
    bst.put(3)
    bst.put(5)
    bst.put(7)
    bst.put(9)
    bst.put(11)
    bst.put(13)
    bst.put(15)
    depths = create_level_lists(bst)
    for d in depths:
        d.show()
    print("------------------------------------")
    bst.put(16)
    bst.put(17)
    depths = create_level_lists(bst)
    for d in depths:
        d.show()