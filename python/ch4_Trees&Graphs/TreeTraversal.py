class TreeNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.name) + " R:" + \
               str(self.right) + ')'


class Traversal:
    def __init__(self):
        pass

    def in_order(self, tree_node):
        if tree_node:
            self.pre_order(tree_node.left)
            self.visit(tree_node)
            self.pre_order(tree_node.right)

    def pre_order(self, tree_node):
        if tree_node:
            self.visit(tree_node)
            self.pre_order(tree_node.left)
            self.pre_order(tree_node.right)

    def post_order(self, tree_node):
        if tree_node:
            self.pre_order(tree_node.left)
            self.pre_order(tree_node.right)
            self.visit(tree_node)

    @staticmethod
    def visit(tree_node):
        print(tree_node.name)

