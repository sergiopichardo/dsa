# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

"""
INPUT
- head: Node
- value: str
- index: int

OUTPUT
- result: Node (the head of the resulting linked list)

RULES 
- it should insert a new node with the value into the list at the specified index
- Consider the head of the linked list as index 0
- it should return the head of the resulting list 
- the insertion should be done in place
- assumptions
    - assume the linked list is none-empty
    - assume the index is no greater than the length of the input list 
    - assume the index is NON-negative

EXAMPLES 
E1
- input: 
          0    1    2    3
    head: a -> b -> c -> d
    value: 'x'
    index: 2
          0    1    2    3    4
- output: a -> b -> x -> c -> d

E2
- input: 
    - head: a -> b 
    - value: 'w'
    - index: 0 
- output: w -> a -> b

MENTAL MODEL / SCENARIOS 
Given a linked list, a value and an index, create a node Node with the input value, and insert the new node at the given index in the linked list, in place.

Scenarios 
a -> b -> d -> e 

when do we stop 
- we stop when the current index is None

index 0: (at the start of the list)
- create a node with the input value 
- set the nodes next to the head of the linked list 
- and return the new node

index i: (in the middle of the linked list)
- create a new node with the input value
- store the current_node.next in a variable called next_node
- set the current_node.next to new_node
- set the new_node.next to next_node

index length -1: (at the very end of the list)
- create a node with the input value 
- if the current_node.next is None 
    - set current_node.next to new_node
    - new_node.next to None


ALGORITHM 
- create a new node with the input value 
- if the index is equal to 0 
    - set new_node.next to head
    - return new_node
- set current_node to head
- set current_index to 0

- while current_node is not None 
    - if current_index + 1 is equal to `index`
        - set next_node to current_node.next
        - set current_node.next to new_node
        - set new_node.next to next_node
        - break out of loop
    
    - set current_node to current_node.next
    - increment current_index by 1

- return head 

COMPLEXITY 
- N: the number of nodes in the linked list 
- Time: O(N)
- Space: O(1)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, value, index):
    new_node = Node(value)

    if index == 0: 
        new_node.next = head
        return new_node
    
    current_node = head
    current_index = 0
    while current_node is not None:
        if current_index + 1 == index:
            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
            break
        current_index += 1
        current_node = current_node.next
    return head


# def insert_node(head, value, index):
#     if index == 0:
#         new_head = Node(value)
#         new_head.next = head
#         return new_head
    
#     count = 0
#     current = head
#     while current is not None:
#         if count == index - 1:
#             temp = current.next
#             current.next = Node(value)
#             current.next.next = temp
    
#         count += 1
#         current = current.next
#     return head


# def insert_node(head, value, index, count = 0):
#     if index == 0:
#         new_head = Node(value)
#         new_head.next = head
#         return new_head

#     if head is None:
#         return None

#     if count == index - 1:
#         temp = head.next
#         head.next = Node(value)
#         head.next.next = temp
#         return 
#     insert_node(head.next, value, index, count + 1)
#     return head


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
