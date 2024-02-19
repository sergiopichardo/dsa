# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

"""
INPUT:
- head: Node
- index: int

OUTPUT: 
- Any (The value at the specified index)

RULES 
- it should return the value of the linked list at the specified index
- if the input index is larger than the number of nodes in the linked list, return None
- Assumptions
    - assume only positive integers will be provied as input


EXAMPLES
T1
input: "red" -> "green" -> "blue" -> None, 2
output: "blue"

T2
input: 1 -> 2 -> 3 -> 4 -> None, 1
output: 2

T3
input: head=1 -> 2 -> 3, index=29
output: None

T4
input: head=1 -> 2 -> 3 -> 4 -> None, index=9
output: None

MENTAL MODEL 
- Given a linked list and an index position, return the value of the node at that index position.

SCENARIOS
Given a valid linked list:

1. positive index within the appropriate range is provided 
    - return the value of the node at that index position
2. positive index outside the range is provided 
    - return None
3. The input index is 0 
    - return the value at index 0
4 The input is other than 0
    - 

ALGORITHM
Iterative Algorithm
- set index to 0 
- while current node is not NULL
    - if index is equal to input index 
        - return node.val
    - increment index by 1
    - advance the current node
- return None

COMPLEXITY
Iterative Solution
- N: length of LL
- Time: O(N)
- Space: O(1)

Recursive Algorithm 
given: 
- head: Node
- index: int

- if head is None:
    - return None
- if index is less than or equal to 0
    - return head.val
- return recursive call with `head.next` and `index - 1`


Recursive Solution 
- N: length of LL
- Time: O(N)
- Space: O(N)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def get_node_value(head: Node, index: int):
#     current_index = 0
#     current_node = head 
#     while current_node is not None:
#         if current_index == index:
#             return current_node.val
#         current_node = current_node.next
#         current_index += 1
#     return None



def get_node_value(head: Node, index: int):
    if head is None:
        return None
    if index <= 0:
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