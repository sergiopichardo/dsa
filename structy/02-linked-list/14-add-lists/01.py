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
# #   621
# # + 354
# # -----
# #   975

"""
INPUT 
- head_1: Node
- head_2: Node

OUTPUT
- Node


PROBLEM
Requirements
- the function should return the head of the new linked list representing the sum of the input lists
- the output list should its digits reversed as well 
- you must do this by traversing the linked lists once 

Metadata
- the nodes in the input lists are reversed; 
    - this means the last significant digit is the number in the head

SCENARIOS
1. Handle same length lists 
2. Handle different length lists 
3. Handle carry  
4. Handle final carry

COMPLEXITY 
N: length of list 1 
M: length of list 2 
Time: O(max(n, m))
Space: O(max(n, m))
"""



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# def add_lists(head_1, head_2, carry = 0):
#     if head_1 is None and head_2 is None and carry == 0:
#         return None

#     val_1 = 0 if head_1 is None else head_1.val
#     val_2 = 0 if head_2 is None else head_2.val  
#     sum = val_1 + val_2 + carry
#     next_carry = 1 if sum > 9 else 0
#     digit = sum % 10

#     result = Node(digit)

#     next_1 = None if head_1 is None else head_1.next
#     next_2 = None if head_2 is None else head_2.next

#     result.next = add_lists(next_1, next_2, next_carry)
#     return result


def add_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head

    carry = 0
    current_1 = head_1
    current_2 = head_2
    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if current_1 is not None:
            current_1 = current_1.next
            
        if current_2 is not None:
            current_2 = current_2.next
        
    return dummy_head.next


def print_linked_list(current_node):
    result = []
    while current_node is not None:
        result.append(str(current_node.val))
        current_node = current_node.next
    result = ' -> '.join(result)
    print(result)



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
add_lists(a1, b1)
# 5 -> 7 -> 9


#  7541
# +  32
# -----
#  7573

a1 = Node(1)
a2 = Node(4)
a3 = Node(5)
a4 = Node(7)
a1.next = a2
a2.next = a3
a3.next = a4
# 1 -> 4 -> 5 -> 7

b1 = Node(2)
b2 = Node(3)
b1.next = b2
# 2 -> 3 

add_lists(a1, b1)
# 3 -> 7 -> 5 -> 7
#   39
# + 47
# ----
#   86

a1 = Node(9)
a2 = Node(3)
a1.next = a2
# 9 -> 3

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

add_lists(a1, b1)
# 6 -> 8
#   89
# + 47
# ----
#  136

a1 = Node(9)
a2 = Node(8)
a1.next = a2
# 9 -> 8

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

add_lists(a1, b1)
# 6 -> 3 -> 1
#   999
#  +  6
#  ----
#  1005

a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)
# 6

add_lists(a1, b1)
# 5 -> 0 -> 0 -> 1