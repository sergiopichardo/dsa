class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_values(head: Node):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

print(get_values(a))