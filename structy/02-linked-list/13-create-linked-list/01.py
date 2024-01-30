# create linked list

# Write a function, create_linked_list, that takes in a list of values as an argument. 
# The function should create a linked list containing each item of the list as the values of the nodes. 
# The function should return the head of the linked list.

"""
INPUT: 
- values: List[Any]

OUTPUT: 
- linked_list: Node

RULES 
Tasks
- it should create a linked list containing each item of the input [regular] list of values 
- it should return the head of the linked list 
- it should return None if the list is empty 

Metadata
- the input list can be empty 
- the items in the input list can be of any type (e.g. str, int, float)
- the linked list items must be in the same order as in the input list 

EXAMPLES 
E1 
input: []
output: None 

E2
input: ["a", "b", "c"]
output: "a" -> "b" -> "c" -> None

E2
input: [1, 2, 3]
output: 1 -> 2 -> 3 -> None

MENTAL MODEL 
Given a list of items, create a linked list containing those values in the list items. 

SCENARIOS
1. iterate over the input list
    - When do stop? 
        - Stop when we reach the end of the list 
        - we could use a for loop
2. attaching the nodes of the linked list in the correct order
    - create `head` variable to instantiate the intial Node 
    - create `tail` variable to guide the next node connection 
    - after we have iterate over the list an created the nodes dynamically, set the tail to None
3. returning the head of the linked list
    - once we break out of the loop, we can return the head 
3. returning None when the input list is empty
    - if the input list is empty, then return None

ALGORITHM 
Parameter List
>> `values`: List[Any]

- IF `values` is empty 
    - RETURN None 

- `head` -> Node instantiated with values[0] value
- `tail` -> Node instantiated with None
- `tail.next` -> `head`

- iterate over `values` from 1 - end of list 
    - `new_node` -> Node instantiated with current value 
    - `tail.next` -> `new_node`
    - `tail` -> `new_node`

- tail.next -> None

- RETURN head

COMPLEXITY 
- N: length of list 
- Time: O(N)
- Space: O(N)
"""

from typing import List, Any

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def create_linked_list(values: List[Any]) -> Node:
#     if len(values) == 0:
#         return None
    
#     head = Node(values[0])
#     tail = head

#     for value in values[1:]:
#         new_node = Node(value)
#         tail.next = new_node
#         tail = new_node

#     tail.next = None
#     return head


# def create_linked_list_2(values):
#     dummy_head = Node(None)
#     tail = dummy_head

#     for val in values:
#         tail.next = Node(val)
#         tail = tail.next

#     return dummy_head.next


# time: O(N^2)
# space: O(N)
# def create_linked_list(values):
#     if len(values) == 0:
#         return None
    
#     head = Node(values[0])
#     head.next = create_linked_list(values[1:])  # this creates a new copy of the list 
#     return head

# time: O(N)
# space: O(N)
def create_linked_list(values, i=0):
    if i == len(values):
        return None
    head = Node(values[i])
    head.next = create_linked_list(values, i + 1)
    return head

def print_linked_list(current_node):
    result = []
    while current_node is not None:
        result.append(str(current_node.val))
        current_node = current_node.next

    if len(result) == 0:
        print(None)
        return

    result = ' -> '.join(result)
    print(result)


print_linked_list(create_linked_list(["h", "e", "y"]))
# # h -> e -> y
print_linked_list(create_linked_list([1, 7, 1, 8]))
# # 1 -> 7 -> 1 -> 8
print_linked_list(create_linked_list(["a"]))
# a
print_linked_list(create_linked_list([]))
# None