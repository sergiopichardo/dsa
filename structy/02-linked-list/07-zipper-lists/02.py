# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

"""
INPUT: 
- head1: Node
- head2: Node

OUTPUT: 
- head Node (merged linked list)

RULES
- it should zipper the two lists together into a single linked list by alternating nodes
- if one of the linked lists is longer than the other, the resulting linked list should terminate with the remaining nodes
- it should return the head of the zippered linked list 
- it should be done in place, by mutating the original nodes

Assumptions
- Assume both lists are non-empty

Questions
Q1) alternating nodes? 
E1
input:
--> L1: a -> b -> c -> None
--> L2: x -> y -> z -> None
output: 
--> a -> x -> b -> y -> c -> z -> None

Q2) terminating with remaining nodes? 
E2
input: 
--> L1: a -> b -> c -> d -> None 
--> L2: x -> y -> None
output: 
--> a -> x -> b -> y -> c -> d -> None 
we simply attach the remaining nodes of the longer linked list at the end of the alternating list

Q3) in place? 
This means we're using the original nodes from each list and we're not creating a linked list from scratch.

SCENARIOS 
1. iterating over both lists 
2. advance to the next nodes
2. alternating nodes
3. attaching remaining nodes to shorter list
4. return the head of the linked list


ALGORITHM 
previous = a
            p1
--> L1: a -> b -> c -> None
        p2
--> L2: x -> y -> z -> None

SET previous = head_1
SET counter = 0
current_node_1 = head_1.next
current_node_2 = head_2

WHILE the current_node_1 is not None and current_node_2 is not None keep going
    IF counter is even
        SET previous.next to current_node_1
        current_node_1 = current_node_1.next
    IF counter is odd
        SET previous.next to current_node_2
        current_node_2 = current_node_2.next
    previous = previous.next
    INCREMENT the counter by 1 

IF current_node_1 is not None
    previous.next = current_node_1

if current_node_2 is not None
    previous.next = current_node_2

return head_1



COMPLEXITY 
n = length of list 1
m = length of list 2
time: O(min(n, m))
space: O(1)
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def zipper_lists(head_1: Node, head_2: Node):
    previous = head_1
    current_node_1 = head_1.next
    current_node_2 = head_2
    alternating_position = 0

    while current_node_1 is not None and current_node_2 is not None:
        if alternating_position % 2 == 0: 
            previous.next = current_node_2
            current_node_2 = current_node_2.next
        else: 
            previous.next = current_node_1
            current_node_1 = current_node_1.next
        
        previous = previous.next
        alternating_position += 1

    if current_node_1 is not None: 
        previous.next = current_node_1
    if current_node_2 is not None: 
        previous.next = current_node_2
    return head_1


## Recursive solution 


def print_ll(node: Node):
    result = []
    while node is not None:
        result.append(str(node.val))
        node = node.next
    result.append('None')
    print(' -> '.join(result))


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print_ll(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z






s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

print_ll(zipper_lists(s, one))
# s -> 1 -> t -> 2 -> 3 -> 4




w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

print_ll(zipper_lists(w, one))
# w -> 1 -> 2 -> 3