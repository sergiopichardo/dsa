# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

"""
INPUT:
> head: linked list head 
> index: the position of the target item in the linked list

OUTPUT: 
- The `value` at the specified index OR `None`

RULES 
- return the value of the linked list node at the specified index. Otherwise, return None.

MENTAL MODEL 
- Return the node value specified at the index position in the linked list. If there is no node at the given index, return None.

ALGORITM 
>> High Level
- Loop over linked list 
- count from 0 to end of linked list to assign positions 
- compare the current index with target index 
- if there's a node with a value, return the value
- if we finish iterating over list and no value is found, return none

>> Mid Level 
- set count to 0
- while the current node is not none
    - if the current node at the specified index has a value
        - return the value 
    - move onto the next node
    - increment count by 1 
- return false 


COMPLEXITY 
- N: the number of nodes 
- Time: O(N)
- Space: O(1)
"""

from typing import Any

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def get_node_value(head: Node, target_index: int) -> Any | None:
#     current_index = 0
#     current_node = head
#     while current_node is not None:
#         if current_index == target_index:
#             return current_node.val
#         current_node = current_node.next
#         current_index += 1
#     return None


# N: number of nodes 
# Time: O(N)
# Space: O(N)
# def get_node_value(head, index, current_index=None):
#     if current_index is None:
#         current_index = 0

#     if head is None:
#         return None
    
#     if current_index == index:
#         return head.val
    
#     return get_node_value(head.next, index, current_index + 1)

# index: 2
# 2 - 1 = 1
# 1 - 1 = 0 
#           V
# a -> b -> c -> d -> None

def get_node_value(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val

    return get_node_value(head.next, index - 1)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 7)) # None


node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

print(get_node_value(node1, 1)) # 'mango'