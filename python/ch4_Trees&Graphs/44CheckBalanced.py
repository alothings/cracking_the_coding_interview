from TreeTraversal import BST

def get_height(root):
    if root is None: return -1
    return max(get_height(root.left), get_height(root.right)) + 1

def is_balanced(root):
    if root is None: return True
    height_diff = get_height(root.left) - get_height(root.right)
    print("First", height_diff)
    if abs(height_diff) > 1:
        print(height_diff)
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)


tree = BST()
# arr = [1, 2, 3, 4, 5, 6, 7]
arr = [4, 2, 1, 3, 5, 6, 7]
for i in arr:
    tree.add(i)

# # print("In order: ", tree.in_order(tree.root))
# prinat("In order: ", tree.in_order(tree.root))
# print("Pre order: ", tree.pre_order(tree.root))
# print("Post order: ", tree.post_order(tree.root))
print("tree root: ", tree.root)
print("Total height: ", get_height(tree.root))
print(is_balanced(tree.root))

