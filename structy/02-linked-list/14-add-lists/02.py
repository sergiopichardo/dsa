# add lists
# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

# Say we wanted to compute 621 + 354 normally. The sum is 975:

#    621
#  + 354
#  -----
#    975

# Then, the reversed linked list format of this problem would appear as:

#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9
#   621
# + 354
# -----
#   975

"""
INPUT: 
- head_1: Node
- head_2: Node

OUTPUT
- Node (head of the resulting linked list)

RULES 
- the nodes in the input lists are reversed
    - meaning the last significant digit of the number is the head
- returns a new LL head representing the sum of the input LLs 
- the output list should have its digits reversed too


SCENARIOS 
1. Handle same length lists
2. Handle diff length lists 
3. Handle carry 
4. Handle final carry



COMPLEXITY
N = length of list 1
M = length of list 2 
Time = O(max(N, M))
Space = O(max(N, M))
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def print_linked_list(current_node):
    result = []
    while current_node is not None:
        result.append(str(current_node.val))
        current_node = current_node.next

    result.append('None')
    result = ' -> '.join(result)
    print(result)


def add_lists(head_1: Node, head_2: Node, carry: int = 0) -> Node:
    if head_1 is None and head_2 is None and carry == 0:
        return None

    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val  
    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0
    digit = sum % 10

    result = Node(digit)

    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    result.next = add_lists(next_1, next_2, next_carry)
    return result

#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

print_linked_list(add_lists(a1, b1))
# 5 -> 7 -> 9