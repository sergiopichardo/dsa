# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue_list(head):
    target_value = head.val
    current_node = head.next
    while current_node is not None:
        if target_value != current_node.val:
            return False
        current_node = current_node.next
    return True


a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7
print(is_univalue_list(a)) # True


a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4
print(is_univalue_list(a)) # False


u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

print(is_univalue_list(u)) # True
u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 3 -> 3 -> 2
print(is_univalue_list(u)) # False

z = Node('z')
# z

print(is_univalue_list(z)) # True


u = Node(2)
v = Node(1)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 1 -> 2 -> 2 -> 2
print(is_univalue_list(u)) # False