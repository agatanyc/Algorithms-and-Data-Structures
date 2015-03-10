class Node:
    def __init__(self, item, left=None, right=None):
        """(Node, object, Node, Node) -> NoneType"""

        self.item = item
        self.left = left
        self.right = right

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

tree = Node(1, Node(2), Node(3))
print(tree.depth())



