
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None

def print_list(head: Node):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

def print_list_recursive(head: Node):
    if head is None:
        return
    
    print(head.val)
    return print_list_recursive(head.next)

print_list(a)
# print_list_recursive(a)