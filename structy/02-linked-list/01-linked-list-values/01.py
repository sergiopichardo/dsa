# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ


"""
INPUT: LinkedListNode
OUTPUT: List[str]

RULES
- it should return a list containing all values of the nodes in the linked list

MENTAL MODEL 
- we need to extract the letter in each linked list node and return a list with all the letters in the linked list.

DATA STRUCTURE 
- list: to store all letters in the list 

ALGORITHM 
- SET result to []
- LOOP over each item in the linked list 
- APPEND the value to a result list 
- RETURN the result list  

COMPLEXITY 
- N: Number of nodes 
- Time: O(N) 
- Space: O(N)
"""

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def linked_list_values(head: Node) -> List[str]:
#     result = []
#     current_node = head
#     while current_node is not None:
#         result.append(current_node.val)
#         current_node = current_node.next
#     return result

# def linked_list_values(head):
#   values = []
#   _linked_list_values(head, values)
#   return values

# def _linked_list_values(head, values):
#   if head is None:
#     return
#   values.append(head.val)
#   _linked_list_values(head.next, values)

def linked_list_values(head: Node, result: List[str] = None) -> List[str]:
    if result is None:
        result = []

    # base case
    if head is None:
        return result

    # recursive case 
    result.append(head.val)
    return linked_list_values(head.next, result)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]



x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(linked_list_values(x)) # -> [ 'x', 'y' ]

q = Node("q")
# q

print(linked_list_values(q)) # -> [ 'q' ]
print(linked_list_values(None)) # -> [ ]