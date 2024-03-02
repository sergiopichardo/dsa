# remove node
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.
# You may assume that the input list is non-empty.
# You may assume that the input list contains the target.

"""
INPUT
- head: Node (the head of the linked list)
- target: Any (the target value in the node to remove)

OUTPUT
- returns the head of the modified linked list 

RULES 
- it should delete the node containing the target value form the LL
- if the target appears multiple times in the LL, only remove the first instance of the target in the LL
- the LL is non-empty
- the LL contains the target value

ALGORITHM 
Parameters: 
- head: Node
- target: Any (e.g. int, str)

- if the head of the linked list contains the target
    - return head.next


a -> b -> c -> d -> d -> None, "d"

- SET `current_node` to `head`
- SET `previous_node` to None

- while the current_node is not None
    IF current_node's value is EQUAL TO the target
        SET previous_node's next TO current_node's next
        break
    SET previous_node to the current_node
    SET current_node to the next Node 

RETURN head
"""


from typing import Any

class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None


def remove_node(head: Node, target: Any):
    if head.val == target:
        return head.next

    previous_node = None
    current_node = head
        
    while current_node is not None:
        if current_node.val == target:
            previous_node.next = current_node.next
            break
        previous_node = current_node
        current_node = current_node.next
    
    return head

def print_list(node: Node):
    result = []

    while node is not None:
        result.append(str(node.val))
        node = node.next

    result.append('None')
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


x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

# x -> y -> z
print_list(remove_node(x, "z"))
# x -> y



q = Node("q")
r = Node("r")
s = Node("s")

q.next = r
r.next = s

# q -> r -> s
print_list(remove_node(q, "q"))
# r -> s


node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")

node1.next = node2
node2.next = node3
node3.next = node4

# h -> i -> j -> i
print_list(remove_node(node1, "i"))
# h -> j -> i


t = Node("t")

# t
print_list(remove_node(t, "t"))
# None
