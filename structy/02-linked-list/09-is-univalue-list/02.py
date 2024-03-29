# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty

"""
INPUT
- head: Node

OUTPUT
- boolean

RULES
- it should return a boolean indicating whether all the nodes in the linked list have the same value 
    - TRUE: 1 -> 1 -> 1 -> 1 -> None 
    - FALSE: 1 -> 2 -> 2 -> 3 -> None
- Assume the input LL is non-empty
    - we'll never get a node like this: Node(None)

MENTAL MODEL 
- Compare the first value of the linked list to all the others
- if there's a different value along the way return FALSE
- if we get to the end of the list return true 

ALGORITHM 
- IF linked list has exactly one value 
    - return TRUE

- SET compare_node to first node of linked list
- WHILE the current node is not None
    - IF current_node.val is NOT equal to compare_node.val
        - RETURN FALSE
    - advance to the next node
- RETURN TRUE 

COMPLEXITY (iterative)
- N: Length of linked list 
- Time: O(N)
- Space: O(1)

COMPLEXITY (recursive)
- N: Length of linked list 
- Time: O(N)
- Space: O(1)
"""

from typing import Any


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None


def is_univalue_list(head: Node) -> bool:
    if head.next is None:
        return True

    compare_node = head
    current_node = head.next
    while current_node is not None:
        if compare_node.val != current_node.val:
            return False
        current_node = current_node.next
    return True


def is_univalue_list_recursive(head: Node):
    if head is None:
        return True

    if (head and head.next) and head.val != head.next.val:
        return False

    return is_univalue_list_recursive(head.next)


# other solutions
# def is_univalue_list(head):
#     current = head
#     while current is not None:
#         if current.val != head.val:
#             return False
#         current = current.next
#     return True


# def is_univalue_list(head, prev_val=None):
#     if head is None:
#         return True
#     if prev_val is None or head.val == prev_val:
#         return is_univalue_list(head.next, head.val)
#     else:
#         return False


a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7
print(is_univalue_list_recursive(a))  # True


a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4
print(is_univalue_list_recursive(a))  # False


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

print(is_univalue_list_recursive(u))  # True
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
print(is_univalue_list_recursive(u))  # False

z = Node("z")
# z

print(is_univalue_list_recursive(z))  # True


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
print(is_univalue_list_recursive(u))  # False
