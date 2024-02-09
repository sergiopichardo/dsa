"""
Insertion:
- [ ] At the beginning: Add a new node as the first node of the list.
- [ ] At the end: Append a new node to the end of the list.
- [ ] After a given node: Insert a new node after a specified node in the list.
- [ ] Before a given node: Insert a new node before a specified node in the list (requires traversal to find the previous node).
- [ ] At a specific position: Insert a new node at a specified index, requiring traversal to the appropriate point.

Deletion
- [ ] From the beginning: Remove the first node of the list.
- [ ] From the end: Remove the last node of the list, requiring traversal to the second-to-last node.
- [ ] A given node: Remove a specified node from the list, which may involve finding the previous node to adjust links.
- [ ] At a specific position: Remove the node at a specified index, similar to deletion of a given node but located by index.

Traversal:
- [ ] Linear traversal: Sequentially access each node of the list, typically used for operations like printing all elements or calculating the sum of all elements.

Search:
- [ ] Find by value: Look through the list to find a node containing a specified value.
- [ ] Find by position: Access a node at a specific index, requiring linear traversal from the beginning.

Modification:
- [ ] Update the value of a node: Change the data in one or more nodes, which might require traversal if the node is not directly accessible.
Sorting:

List sorting: 
- [ ] Reorder the nodes in the list based on their values, which can be more complex due to the lack of direct access to arbitrary elements.

Reversal: 
- [ ] Reverse the list: Change the direction of the list so that the last node becomes the first node and vice versa, requiring the re-linking of nodes in the opposite direction.

Size: 
- [ ] Length of the list: Calculate the number of nodes in the list, which generally requires a full traversal to count each node.

Utility Operations:
- [ ] Empty the list: Remove all nodes from the list, effectively clearing it.
- [ ] Check if the list is empty: Determine if the list has no nodes.
"""


class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# Singly Linked List
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d


