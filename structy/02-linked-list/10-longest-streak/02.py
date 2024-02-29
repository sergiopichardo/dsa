# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument. 
# The function should return the length of the longest consecutive streak of the same value within the list

"""
INPUT
- head: Node 

OUTPUT
- total_streak: int 

RULES
Explicit
- it should return the length of the longest consecutive streak of the same value within the list 
- what is a longest consecutive streak? 
    --> 1 -> 1 -> 2 -> 2 -> 2 -> 3 -> None 
    --> the longest streak would be 3, because 2 appears 3 times consecutively

Implicit 
- you can have an empty linked list as input e.g. Node(None) 
    - In that case the longest streak would be 0

EXAMPLES 

max_streak: 4
current_streak: 1
current_node: head
1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> None 
if current node is None or current.next is None (return 0)
None 

MENTAL MODEL 
maintain two variables:
- `current_streak` to count the number of times a value appears consecutively 
- `max_streak` to count the max times a value has appeared consecutevly int total (after we've gone through the entire list)
- we'll need to check if the current node is None

SCENARIOS
1. check for the edge case of an empty list
2. keeping track of the linked list consecutive values
    - `current_streak` and `max_streak`
3. know how to traverse the linked list 
4. return the integer result 

ALGORITHM
parameters: 
- head: Node

IF `head` is None
    RETURN 0
IF `head` is not None and `head.next` is None
    RETURN 1 

SET max_streak to 1
SET current_streak to 1
SET previous_node to head
SET current_node to head.next

WHILE current_node is not None
- IF the current_node's value is equal to the next node's value 
    INCREMENT current_streak by 1 
    IF current_streak is greater than max_streak
        SET max_streak to current_streak
    OTHERWISE 
        SET current_streak to 1
    SET previous_node to current_node
    SET current_node to the next node

- RETURN max_streak

COMPLEXITY
- N: number of nodes in the linked list 
- Time: O(N)
- Space: O(1)
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def longest_streak(head: Node):
    if head is None: 
        return 0
    # if head is not None and head.next is None:
    #     return 1
    
    max_streak = 1
    current_streak = 1
    previous_node = head
    current_node = head.next

    while current_node is not None:
        if previous_node.val == current_node.val:
            current_streak += 1
            if current_streak > max_streak: 
                max_streak = current_streak
        else:
            current_streak = 1
            
        previous_node = current_node
        current_node = current_node.next

    return max_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6
print(longest_streak(a)) # 3


a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 3 -> 3 -> 3 -> 9 -> 9
print(longest_streak(a)) # 4





a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9
print(longest_streak(a)) # 3




a = Node(5)
b = Node(5)

a.next = b

# 5 -> 5

print(longest_streak(a)) # 2
a = Node(4)

# 4

print(longest_streak(a)) # 1
print(longest_streak(None)) # 0