# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

"""
INPUT: 
- head_1: Node (head of list 1)
- head_2: Node (head of list 2)

OUTPUT: 
- Node (head of zippered list) 

RULES 
- it should zipper two lists together into a single linked list by alternating nodes. 
- the nodes of the longest list should be attached to the end of the resulting list. 
- the function should return the head of the zippered list 
- we should always start with the first node of list 1 
- assume we'll always be given a linked list of size one
    - we'll never get None as the input for either or both lists

MENTAL MODEL 
Combine in-place the nodes of two lists such that they alternate between list 1 and list 2. 
So, if we have list 1 with notes A -> B -> C and list 2 with notes U -> V -> W -> X -> Y -> Z. 
The expected result should be a single linked list that looks like this: 
A -> U -> B -> V -> C -> W -> X -> Y -> Z. Where the nodes of the longer list are attached to the 
end of the resulting linked list.


ALGORITHM 

- linked list traversal
    - what is the stopping condition? 
- alternate b/w lists
    - We could use even/odd logic 
        - if even we get the node from list 1 
        - if odd we get the node from list 2
- attaching to shorter list 
    - where do we do this? outside the loop? 
- returning the head of the new merged list 


COMPLEXITY 
- N: number of nodes of list 1 
- M: number of nodes of list 2 
- Time: O(min(N, M))
- Space: O(1)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head_1, head_2):
    tail = head_1
    current_1 = head_1.next
    current_2 = head_2
    count = 0

    while current_1 is not None and current_2 is not None:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next
        tail = tail.next
        count += 1
        
    if current_1 is not None:
        tail.next = current_1
    if current_2 is not None:
        tail.next = current_2
        
    return head_1

# def zipper_lists(head_1, head_2):
#     if head_1 is None and head_2 is None:
#         return None
#     if head_1 is None:
#         return head_2
#     if head_2 is None:
#         return head_1
    
#     next_1 = head_1.next
#     next_2 = head_2.next

#     head_1.next = head_2
#     head_2.next = zipper_lists(next_1, next_2)
#     return head_1  

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

print(zipper_lists(a, x))
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

print(zipper_lists(s, one))
# s -> 1 -> t -> 2 -> 3 -> 4




w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 

print(zipper_lists(w, one))
# w -> 1 -> 2 -> 3