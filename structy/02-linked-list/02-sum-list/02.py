# Sum list
# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.


"""

INPUT: 
- head: Node

OUTPUT: 
- total_sum: int

RULES 
- it should return the total sum of all values in the linked list 
- if the linked list is None, return 0
- if the linked list only has 1 element, return the element itself

EXAMPLES
T1
input: 1 -> 2 -> 3 -> None
output: 6

T2
input: None
output: 0

T3
input: 2000 -> None
output: 2000

SCENARIOS
1. when do we stop iterating? 
    - We stop iterating when the current node is None
2. How do we move onto the next node? 
    - we set the current node to the NEXT node
3. what happens if the LL is empty? 
    - we return 0


ALGORITHM (iterative)
FUNC sum_list (head: Node)
- SET a total sum variable to 0
- WHILE the current node is not NULL
    - ADD up to the total sum
    - ADVANCE the current node
- RETURN the total sum
ENDFUNC

COMPLEXITY
- N: number of nodes in the linked list
- Time: O(N)
- Space: O(1)

ALGORITHM (recursive)

FUNC sum_list (head: Node)
    - IF the current node is empty
        - RETURN 0
    - ADD the current node value plus the recursively call to `sum_list` with the next node 
ENDFUNC

COMPLEXITY
- N: number of nodes in the linked list
- Time: O(N)
- Space: O(N)
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


# iterative
# def sum_list(head: Node):
#     total = 0
#     current_node = head
#     while current_node is not None:
#         total += current_node.val
#         current_node = current_node.next
#     return total

# recursive 
def sum_list(head: Node):
    if head is None:
        return 0
    return head.val + sum_list(head.next)



a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19


x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

print(sum_list(x)) # 42


z = Node(100)

# 100

print(sum_list(z)) # 100
print(sum_list(None)) # 0