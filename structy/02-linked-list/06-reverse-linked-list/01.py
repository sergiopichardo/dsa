# reverse list

# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

"""
INPUT
- head: linked list node

OUTPUT
- reversed linked list 

RULES 
- reverse the linked list "in-place"
    - it mutates the original linked list 
- return the head of the reversed linked list 

Assumptions
- A non-empty linked list will be provided
    - A linked list with at least one node

MENTAL MODEL 
What is a (singly) linked list?
- A linked list is an object that usually has a value and a reference to the next object. 
- The first node of a linked list is known as the "head". 
- The last node of a linked list is known as the "tail", and it has a reference to None. It marks the end of the linked list.

What are we trying to accomplish? 
input: "a" -> "b" -> "c" -> "d" -> None
output: "d" -> "c" -> "b" -> "a" -> None

We need to keep track of 3 key pieces of information (keep references to): 
1. the `previous` node: 
    - previous will be a temporary variable that will store the reverse linked list
2. the `current` node: 
    - this will give us access to the next reference, and flip it
3. the `next` node: 
    - this will store the rest of the linked list 

ALGORITHM 
>> high-level algorithm
1. traverse the linked list 
2. flip the references by pointing "current_node.next" to the previous node
3. return the head of the mutated original linked list

>> mid-level 


"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head: Node) -> Node:
    prev = None
    current = head

    while current is not None: 
        next_node = current.next    # store the next node 
        current.next = prev         # reverse the pointer of the current node
        # keep advancing the list
        prev = current              # move prev to current 
        current = next_node         # advanced current to next node 

    return prev


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

print(reverse_list(a)) # f -> e -> d -> c -> b -> a -> None


x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(reverse_list(x)) # y -> x -> None
p = Node("p")

# p

print(reverse_list(p)) # p -> None