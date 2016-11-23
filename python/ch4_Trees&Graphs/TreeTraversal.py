class TreeNode:
    def __init__(self, name, left=None, right=None, parent=None):
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        # return '(' + str(self.left) + ':L ' + "V:" + str(self.name) + " R:" + \
        #        str(self.right) + ')'
        return str(self.name)

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        treenode = TreeNode(value)
        if self.root is None:
            self.root = treenode
        else:
            buff = self.root
            current = self.root
            while current is not None:
                if current.name < value:
                    buff = current
                    current = current.right
                    #
                    # if current.left:
                    #     current = current.left
                    # else:
                    #     current.left = TreeNode(value)
                    #     break
                else:
                    buff = current
                    current = current.left
                    # if current.right:
                    #     current = current.right
                    # else:
                    #     current.right = TreeNode(value)
                    #     break
            if buff.name < value:
                buff.right = treenode
                treenode.parent = buff
            else:
                buff.left = treenode
                treenode.parent = buff

    def in_order(self, tree_node):
        if tree_node:
            self.in_order(tree_node.left)
            # self.visit(tree_node)
            print(tree_node.name)
            self.in_order(tree_node.right)

    def pre_order(self, tree_node):
        if tree_node:
            # self.visit(tree_node)
            print(tree_node.name)
            self.pre_order(tree_node.left)
            self.pre_order(tree_node.right)

    def post_order(self, tree_node):
        if tree_node:
            self.post_order(tree_node.left)
            self.post_order(tree_node.right)
            # self.visit(tree_node)
            print(tree_node.name)

    @staticmethod
    def visit(tree_node):
        print(tree_node.name)

# tree = BST()
# arr = [8,3,1,6,4,7,10,14,13]
# for i in arr:
#     tree.add(i)
#
# print("In order: ", tree.in_order(tree.root))
#
