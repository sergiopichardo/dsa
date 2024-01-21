# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

"""
INPUT: linked list head 
OUTPUT: integer 

RULES 
- it should return the total sum of all values in the linked list 
- the value of each node is an integer
- assumptions: 
    - A valid linked list with valid nodes will always be provided 
    - each node will have an integer value (+, -)

EXAMPLES 
T1
input: A(1) -> B(2) -> C(3) -> D(4) -> None
output: 10 
explanation: 1 + 2 + 3 + 4 = 10

T2
input: A(1) -> B(300) -> Node
output: 300
explanation: 1 + 300 = 301

MENTAL MODEL
- given a linked list of nodes containing a value, sum all the values and return the integer result

ALGORITHM 
High Level Algorithm 
- iterate over the linked list
- aggregate values
- return the total 

Mid level algorithm 
- set `total` to 0 (zero)
- while loop to traverse the list 
    - check if the current value is not Node 
    - Add the value of the current node to `total`
    - move to the next node 
- return `total`

Low level algorithm 
>> traversal logic: 
- use a while loop to iterate until `current_node` is None
    - Inside the loop: 
        - increment `total` by current node value 
        - move to the next node by setting current_node to current_node.next

COMPLEXITY
- N: each node in the linked list 
- Time: O(N)
- Space: O(1)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def sum_list(head: Node) -> int:
#     total = 0
#     current_node = head

#     while current_node is not None:
#         total += current_node.val
#         current_node = current_node.next

#     return total

# def sum_list(head: Node, result: int = None) -> int:
#     if result is None:
#         result = 0
#     if head is None:
#         return result 
#     return sum_list(head.next, result + head.val)
        

# Time: O(N) 
# Space: O(N) - stack frame results in linear space
def sum_list(head): 
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