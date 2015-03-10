"""Confirms that given data structure is a binary search tree"""
from collections import namedtuple

Node = namedtuple("Node", ["value", "left", "right"])

def contains(tree, x):
    if not tree:
        return False
    if x == tree.value:
        return True
    if x < tree.value:
        return contains(tree.left, x)
    else:
        return contains(tree.right, x)

def contains1(tree, x):
    return tree and (
            x == tree.value or (
                contains(tree.left, x) if x < tree.value else
                contains(tree.right, x)))

if __name__ == '__main__':
    tree = Node(4,
            Node(2,
                Node(1, None, None),
                Node(3, None, None)),
            Node(6,
                Node(5, None, None),
                Node(7, None, None)))

    assert(contains(tree, 4))
    assert(not contains(tree, 18))
    assert(contains1(tree, 4))
    assert(not contains1(tree, 18))

    print(contains(tree, 4))
    print(not contains(tree, 18))
    print(contains1(tree, 4))
    print(not contains1(tree, 18))
