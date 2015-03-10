class Node():
    """Sample binary node class"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#def print_tree(tree):
#    """Prints the given tree starting from the root"""
#    array = [tree]
#    level = 0
#    while array:
#        for root in array[:]:
#            if root:
#                print(root.value, end='')
#                array.append(root.left)
#                array.append(root.right)
#            array.pop(0)
#        print()

def print_tree(root):
    c = 0               # current depth
    q = [(root, 0)]     # queue of node/depth pairs
    while q:
        n, d = q.pop(0) # node, depth
        if n:
            if d > c:
                print()
                c = d
            print(n.value, end='')
            q += ((n.left, d + 1), (n.right, d + 1))
    print()

my_tree = Node(3,
            Node(2,
                Node(5,
                    Node(3),
                    Node(0)),
                Node(6,
                    Node(3),
                    Node(1))),
           Node(4,
               Node(7,
                   Node(2), Node(8)),
               Node(9,
                   Node(5), Node(7))))

print_tree(my_tree)
