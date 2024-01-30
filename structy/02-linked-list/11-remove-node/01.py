# remove node
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.
# You may assume that the input list is non-empty.
# You may assume that the input list contains the target.

"""
INPUT
- head: Node 
- target_val: str (letter)

RULES 
- it should delte the node containig the target value from the linked list 
- return the head of the resulting linked list 
- if the target appears multiple times, only remove the first instance of the target
- Do this in place 
- assume the list is non-empty, and it contains the target

EXAMPLE 
T1
A -> B -> C -> D -> None

input: A -> B -> C -> D -> None, B
output: A -> C -> D -> None

T2
input: A -> B -> C -> B -> D -> None, B
output: A -> C -> B -> D -> None
because: we only remove the first "B"

T3
input: A -> None, A
output: None 
because: A is the target and it has been removed

T4
input: A -> B -> C -> None, A
output: B -> C -> None

EXPLORATION 
prev = A 

A -> B -> C -> D -> 
prev.next = current.next
current.next = None

MENTAL MODEL 
We need to traverse the linked list and find the first occurrance of the target 
value and remove it. 

NOTES
- we'll need to track the previous and the current nodes
- we'll need to have a boolean flag, so we can track the first occurrance of the target instance

ALGORITHM 
---- High Level ---- 
1. track the first occurrence has been found 
2. traverse the linked list and know when to stop 
    - 
3. perform the removal operation 
    special cases
        - the target val is the head of linked list 
        - the target val is the tail of linked list 
        - the target val is in the middle of the linked list 
4. return the head of the modified linked list

---- Mid Level ----
Given the arguments: 
> head: Node 
> target_value: str

- if `head.val` is equal to `target_value`
    - return `head.next`

- SET `current_node` to `head` 
- SET `prev_node` to Node 

- while `current_node` is not None
    - if `current_node.val` is equal to `target_value`: 
        - set `prev_node.next` to `current_node.next`
        - break out of loop
    - set `current_node` to `current_node.next`
    - set `prev_node` to current_node
- return `head`


COMPLEXITY 
- N: the number of nodes in the linked list 
- Time: O(N) 
- Space: O(1)

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# def remove_node(head, target_val):
#     if head.val == target_val:
#         return head.next
    
#     current_node = head
#     prev_node = None

#     while current_node is not None:
#         if current_node.val == target_val:
#             prev_node.next = current_node.next 
#             break
#         prev_node = current_node
#         current_node = current_node.next 
#     return head


# COMPLEXITY 
# - N: the number of nodes in the linked list 
# - Time: O(N) 
# - Space: O(N)
def remove_node(head, target_val):
    if head is None:
        return None
    if head.val == target_val:
        return head.next
    head.next = remove_node(head.next, target_val)
    return head    



def print_list(head):
    result = []
    current_node = head
    while current_node is not None:
        result.append(str(current_node.val))
        current_node = current_node.next
    print(' -> '.join(result))


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
print_list(remove_node(a, "c"))


# # a -> b -> d -> e -> f
# x = Node("x")
# y = Node("y")
# z = Node("z")

# x.next = y
# y.next = z

# # x -> y -> z

# remove_node(x, "z")
# # x -> y
# q = Node("q")
# r = Node("r")
# s = Node("s")

# q.next = r
# r.next = s

# # q -> r -> s

# remove_node(q, "q")
# # r -> s
# node1 = Node("h")
# node2 = Node("i")
# node3 = Node("j")
# node4 = Node("i")

# node1.next = node2
# node2.next = node3
# node3.next = node4

# # h -> i -> j -> i

# remove_node(node1, "i")
# # h -> j -> i
# t = Node("t")

# # t

# remove_node(t, "t")
# # None