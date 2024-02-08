from typing import Any

class Deque(object):
    def __init__(self) -> None:
        self.items = []

    def add_front(self, item) -> None:
        self.items.append(item)

    def add_rear(self, item) -> None:
        self.items.insert(0, item)

    def remove_front(self) -> Any:
        return self.items.pop()

    def remove_rear(self) -> Any:
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)


d = Deque()

d.add_front('hello')
d.add_rear('world')

print(d.size())

print(d.remove_front() + ' ' + d.remove_rear())

print(d.size())

print(d.is_empty())