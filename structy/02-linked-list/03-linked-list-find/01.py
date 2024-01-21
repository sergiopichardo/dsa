# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

"""
INPUT: Node, str
OUTPUT: boolean 

RULES 
- it should return a boolean indicating whether or not the linked list contains the target

MENTAL MODEL 
- given a linked list where each node has some arbitrary value, return true if the value of some node contains the target value. Otherwise, return false.

ALGORITHM 
>> High Level 
- iterate linked list 
- compare current node value with target value 
- return true if found, or false otherwise 
- move onto the next node

>> Mid Level 
- loop (while loop)
    - compare `current_node.val` with `target`
        - return `true` if the values match
    - move to next by setting current_node to current_node.next
- return false if we finished looping and did not find the value

COMPLEXITY
- N: number of nodes in linked list 
- Time: O(N)
- Space: O(1)
"""


# def linked_list_find(head, target):
#     current_node = head

#     while current_node is not None:
#         if current_node.val == target:
#             return True
#         current_node = current_node.next
#     return False


# N: Number of nodes
# Time: O(N)
# Space: O(N)
def linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True

    return linked_list_find(head.next, target)

class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


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
