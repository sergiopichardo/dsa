from typing import Any

class Queue(object):
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        front_item = self.items[0]
        self.items = self.items[1:]
        return front_item

    def isEmpty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.items)
    
queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# queue: ['A', 'B', 'C', 1, 2, 3]

print(queue.size())  # 6
print(queue.isEmpty())  # False 

print(queue.dequeue())  # A
print(queue.dequeue())  # B
print(queue.dequeue())  # C

print(queue.size())  # 3
print(queue.items)  # [1, 2, 3]

