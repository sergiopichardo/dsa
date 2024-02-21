# reverse list

# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

"""


ALGORITHM 

input: a -> b -> c -> d -> None
output: d -> c -> b -> a -> None

set prev_node to None
set current_node to head
while the current_node is not None
    set next_node to current_node.next  <-- save ref to next so we don't lose the rest of LL
    set current_node.next to prev_node 
    prev_node = current_node
    set current_node to next_node
return head
"""

def print_ll(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    print(' -> '.join(result))


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def reverse_list(head: None):
    prev_node = None
    current_node = head 
    while current_node is not None:
        next_node = current_node.next 
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node

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

print_ll(reverse_list(a)) # f -> e -> d -> c -> b -> a -> None


x = Node("x")
y = Node("y")

x.next = y

# x -> y

print_ll(reverse_list(x)) # y -> x -> None
p = Node("p")

# p

print_ll(reverse_list(p)) # p -> None