from typing import Any

class Queue(object):
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        return self.items.pop()

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

#        rear               front
# queue: [3, 2, 1, 'C', 'B', 'A']

print(queue.size())  # 6
print(queue.isEmpty())  # False 

print(queue.dequeue())  # A
print(queue.dequeue())  # B
print(queue.dequeue())  # C

print(queue.size())  # 3
print(queue.items)  # [1, 2, 3]

