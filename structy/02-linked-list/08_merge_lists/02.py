# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

"""
INPUT: 
- head_1: Node
- head_2: Node

OUTPUT
- a single sorted list

RULES 
Explicit 
- it should merge the two lists together into a single sorted linked list
- it should return the head of the merged linked list

Implicit 
- both linked lists are already sorted in increasing order
- you can have repeated values
    example: 3 occurs in both lists
        a: 1 -> 2 -> 3 -> None
        b: 3 -> 4 -> 5 -> None
    

EXAMPLES 
T1
input:
--> 5 -> 7 -> 10 -> 12 -> 20 -> 28
--> 6 -> 8 -> 9  -> 25

output: 
--> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 

SCENARIOS 
1. choose the smallest value in a node
2. create dummy node to make it easier to return head of sorted linked list at the end
3. advance nodes once a node has been attached to the tail
    - advance only the linked list whose node was attached
4. return the head of linked list `dummy_node.next`

# ALGORITHM 
SET `current_node_1` to head_1
SET `current_node_2` to head_2
SET `dummy_node` to Node(None)
SET `tail` to dummy_node

while current_node_1 is not None and current_node_2 is not None
    if current_node_1 is less than current_node_2
        SET tail.next to current_node_1
        set current_node_1 = current_node_1.next
    otherwise
        SET tail.next to current_node_2
        set current_node_2 = current_node_2.next
    tail = tail.next
    
if current_node_1 is not None
    tail.next = current_node_1
if current_node_2 is not None
    tail.next = current_node_2

return dummy_node.next



# COMPLEXITY (iterative)
M: length of LL 2
N: length of LL 1
Time: O(min(M, N))
space: O(1)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head_1: Node, head_2: Node):
    current_node_1 = head_1
    current_node_2 = head_2
    dummy_node = Node(None)
    tail = dummy_node

    while current_node_1 is not None and current_node_2 is not None:
        if current_node_1.val < current_node_2.val:
            tail.next = current_node_1
            current_node_1 = current_node_1.next
        else:
            tail.next = current_node_2
            current_node_2 = current_node_2.next
        tail = tail.next

    if current_node_1 is not None:
        tail.next = current_node_1
    if current_node_2 is not None:
        tail.next = current_node_2

    return dummy_node.next


def merge_lists_recursive(head_1: Node, head_2: Node):
    # base case 
    if head_1 is None and head_2 is None:
        return None
    
    # logic 
    if head_1 is None:
        return head_2
    
    if head_2 is None:
        return head_1
    
    head_2_next = head_2.next

    if head_1.val < head_2.val:
        head_1_next = head_1.next
        head_1.next = merge_lists_recursive(head_1_next, head_2)
        return head_1
    else:
        head_2_next = head_2.next
        head_2.next = merge_lists_recursive(head_1, head_2_next)
        return head_2


def print_ll(node: Node):
    result = []

    while node is not None:
        result.append(str(node.val))
        node = node.next

    print(' -> '.join(result))

    


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

print_ll(merge_lists_recursive(a, q))
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 




# a = Node(5)
# b = Node(7)
# c = Node(10)
# d = Node(12)
# e = Node(20)
# f = Node(28)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # 5 -> 7 -> 10 -> 12 -> 20 -> 28

# q = Node(1)
# r = Node(8)
# s = Node(9)
# t = Node(10)
# q.next = r
# r.next = s
# s.next = t
# # 1 -> 8 -> 9 -> 10

# print_ll(merge_lists(a, q))
# # 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 





# h = Node(30)
# # 30

# p = Node(15)
# q = Node(67)
# p.next = q
# # 15 -> 67

# print_ll(merge_lists(h, p))
# # 15 -> 30 -> 67