# Given an array, return a BST with minimum height
from TreeTraversal import TreeNode

def initial_min_tree(arr):
    # return min_tree(arr, 0, len(arr) - 1)
    return min_tree2(arr)

def min_tree(arr, start, end):
    if start > end: return ''

    m = int((start + end)/2)

    n = TreeNode(arr[m])

    n.left = min_tree(arr, start, m - 1)
    n.right = min_tree(arr, m + 1, end)

    return n


def min_tree2(arr):
    if 0 > len(arr) -1: return ''

    m = int((len(arr)-1)/2)

    n = TreeNode(arr[m])

    # n.left = min_tree(arr, start, m - 1)
    n.left = min_tree2(arr[:m-1])
    n.right = min_tree2(arr[m+1:])

    return n

# a = [1,2,3,4,5,6,7,8]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(initial_min_tree(a))
