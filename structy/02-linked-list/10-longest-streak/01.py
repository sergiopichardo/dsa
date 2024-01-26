# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

"""
INPUT 
- Node (head of a linked list)

OUTPUT 
- int (the longest number of consecutives occurrences)

RULES 
- it should return the longest consecutive streak of the same value
- assume a non-empy linked list head will be given as input
- assume the linked list node values will be an integer (+, - or 0)


EXAMPLES 
T1
- input: 1 -> 2 -> 2 -> 3 -> None
- output: 2
- because: 2 appears a total of 2 times consecutively

T2
- input: 5 -> 6 -> 7 -> 7 -> 7 -> 8 -> None
- output: 3
- because: 7 appears a total of 3 times consecutively

MENTAL MODEL 
Count the longest number of times a number appears consecutively in a linked list. 


ALGORITHM 



COMPLEXITY 
- N: number of nodes 
- Time: O(n)
- Space: O(1)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak(head: Node):

    max_streak = 0
    current_streak = 0
    prev_val = None

    current_node = head
    while current_node is not None: 
        if current_node.val == prev_val:
            current_streak += 1
        else: 
            current_streak = 1
        
        prev_val = current_node.val
        
        if current_streak > max_streak:
            max_streak = current_streak

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