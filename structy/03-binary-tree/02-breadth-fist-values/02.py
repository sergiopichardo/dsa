"""
breadth first values
Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def breadth_first_values(root):
#     if root is None:
#         return []

#     queue = [root]
#     values = []

#     while queue:
#         current = queue.pop(0)
#         values.append(current.val)

#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)

#     return values        

def depth_first_values(root):
    if root is None:
        return []
    
    left_values = depth_first_values(root.left) # [b, d, e]
    right_values = depth_first_values(root.right) # [c, f]
    
    return [ root.val, *left_values, *right_values ]





a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

breadth_first_values(a)
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a = Node("a")

#      a

breadth_first_values(a)
#    -> ['a']
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
x = Node("x")

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

breadth_first_values(a)
#    -> ['a', 'b', 'c', 'x', 'd', 'e']
breadth_first_values(None)
#    -> []
