

class DoublyLinkedListNode(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


# Doubly linked list 
a = DoublyLinkedListNode('a')
b = DoublyLinkedListNode('b')
c = DoublyLinkedListNode('c')
d = DoublyLinkedListNode('d')

a.next = b 
b.prev = a

b.next = c
c.prev = b

c.next = d
d.prev = c

# to create a circular linked list
# d.next = a