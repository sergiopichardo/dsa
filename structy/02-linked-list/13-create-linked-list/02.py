# create linked list

# Write a function, create_linked_list, that takes in a list of values as an argument.
# The function should create a linked list containing each item of the list as the values of the nodes.
# The function should return the head of the linked list.

"""
INPUT
- values: List[Any]

OUTPUT
- the head of the newly created linked list 

RULES 
- it should create a linked list containing each item of the list as the values of the node
- it should return the head of the linked list
- it should create an empty linked list, if the input is an empty list
- the values of the LL can be of any type

EXAMPLES
E1
- input: [1, 2, 3]
- output: 1 -> 2 -> 3 -> None

E2
- input: ['a', 'b']
- output: a -> b -> None

E3
- input: []
- output: None


SCENARIOS
- dummy = Node(None)
- start = None

while loop        
    new_node = Node(current_value)
    dummy.next = new_node
    dummy = new_node

return dummy.next

ALGORITHM

COMPLEXITY

"""

from typing import List, Any


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"Node({self.val}, {self.next})"


def create_linked_list(values: List[Any]):
    dummy_head = Node(None)
    tail = dummy_head

    for current_value in values:
        new_node = Node(current_value)
        tail.next = new_node
        tail = tail.next

    return dummy_head.next

# Time: O(N)
# Space: O(N)
def create_linked_list_recursive(
    values: List[Any], 
    index: int = 0,
):
    # Base case: if the index is equal to the length of values, we've processed all elements.
    if index == len(values):
        return None

    # create a new node for the current values
    new_node = Node(values[index])

    # Recursively create the rest of the linked list and link the current node to it 
    new_node.next = create_linked_list_recursive(values, index + 1)

    # Return the current node, which is now the head of the linked list including its successors
    return new_node


# Time: O(N)
# Space: O(N^2)
def create_linked_list_recursive_2(values: List[Any]):
    if len(values) == 0:
        return None
    
    head = Node(values[0])
    head.next = create_linked_list_recursive_2(values[1:])

    return head

def print_linked_list(node: Node):
    if node is None:
        print(None)
        return

    result = []

    while node is not None:
        result.append(str(node.val))
        node = node.next

    result.append("None")
    print(" -> ".join(result))


print_linked_list(create_linked_list_recursive(["h", "e", "y"]))

# # h -> e -> y
# print_linked_list(create_linked_list([1, 7, 1, 8]))
# # # # 1 -> 7 -> 1 -> 8
# print_linked_list(create_linked_list(["a"]))
# # # a
# print_linked_list(create_linked_list([]))
# # # None
