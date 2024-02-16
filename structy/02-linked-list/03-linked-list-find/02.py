# linked list find
# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

"""
INPUT: 
- head: Node
- target: Any

OUTPUT: 
- boolean

RULES 
- it should return a boolean if the target value is found in the list. Otherwise, return false

ALGORITHM (Iterative)
----------

FUNC linked_list_find(head: Node, target: Any) -> Bool
- WHILE the current node is not NULL 
    - IF the current node has the target value 
        - RETURN TRUE
- RETURN FALSE 
ENDFUNC

COMPLEXITY
- N: number of nodes
- Time: O(N)
- Space: O(1)

ALGORITHM (recursive)
---------

FUNC linked_list_find(head: Node, target: Any) -> Bool
- IF current node is None
    - RETURN FALSE
- IF current node has the target value 
    - RETURN TRUE
- RETURN recursive call to `linked_list_find` with the next node and the target value
ENDFUNC

COMPLEXITY
N: number of nodes in LL
Time: O(N)
Space: O(N)
"""

from typing import Any

class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def linked_list_find(head: Node, target: Any):
    if head is None: 
        return False
    if head.val == target:
        return True
    return linked_list_find(head.next, target)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
print(linked_list_find(a, "c")) # True




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
print(linked_list_find(a, "q")) # False




node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli
print(linked_list_find(node1, "jason")) # True
