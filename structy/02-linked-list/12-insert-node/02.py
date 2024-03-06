# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

"""
INPUT
- head: Node
- value: Any
- index: int

OUTPUT
- return the head of the linked list with the new node inserted

RULES 
- it should insert a new node with the value into the list at the specified index
- consider the head of the LL as index 0
- it should return th head of the resulting LL
- the insertion should be done in place
- the list will always contain a value (never Node(None)) 
- the index will never be greater than the length of the list 

SCENARIOS 
positions where insertion can happen
- insert at the head position 
input: a -> b -> c -> None, "W", 0
output: "W" -> a -> b -> c -> None

if the insertion is at the head 
    new_node.next = current_node
    return new_node

- insert in the middle and the tail position
input: a -> b -> c -> None, "X", 1
output: a -> "X" -> b -> c -> None

current.next = new_node
node.next = current.next

ALGORITHM 

- SET current_node to head
- SET new_node to Node(value)
- SET counter to 0

- IF index is 0 (zero) <---- insertion at the head
    - SET new_node's NEXT to current_node
    - RETURN new_node

- WHILE current node is not NULL    <---- insertion at other
    - IF counter is EQUAL TO index - 1
        - SET current_node's NEXT to new_node
        - SET new_node's NEXT to current_node's NEXT
    - ADVANCE current_node 
    - INCREMENT counter by 1 

- RETURN head

COMPLEXITY (iterative)
- N: length of linked list 
- Time: O(N)
- Space: O(1)
"""


from typing import Any

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def insert_node(head: Node, value: Any, index: int):
    current_node = head
    new_node = Node(value)
    counter = 0

    if index == 0:
        new_node.next = current_node
        return new_node

    while current_node is not None:
        if counter == index - 1: # index will never be -1 cause we already handled the case where insertion is at the heads position 
            next_node = current_node.next
            new_node.next = next_node
            current_node.next = new_node 

        current_node = current_node.next
        counter += 1
    return head 

# COMPLEXITY (Recursive)
# N: Length of LL
# Time: O(N)
# Space: O(N)
def insert_node_recursive(head: Node, value: Any, index: int, counter: int = 0):
    if head is None: 
        return None
    
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node
    
    if counter == index - 1:
        new_node = Node(value)
        next_node = head.next
        new_node.next = next_node
        head.next = new_node
    else:
        insert_node_recursive(head.next, value, counter + 1)

    return head


def print_linked_list(current_node):
    result = []
    while current_node is not None:
        result.append(str(current_node.val))
        current_node = current_node.next

    result = ' -> '.join(result)
    print(result)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
print_linked_list(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d



# 

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
print_linked_list(insert_node(a, 'v', 3))
# a -> b -> c -> v -> d





a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d



# a -> b -> c -> d
print_linked_list(insert_node(a, 'm', 4))
# a -> b -> c -> d -> m




a = Node("a")
b = Node("b")

a.next = b

# a -> b
print_linked_list(insert_node(a, 'z', 0))
# z -> a -> b
