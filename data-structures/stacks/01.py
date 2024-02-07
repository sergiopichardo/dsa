class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        top_item = self.items[self.size()-1]
        return top_item

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
    

stack = Stack()

print(stack.size())
print(stack.isEmpty())

stack.push('a')
stack.push('b')
stack.push('c')

print(stack.size())
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
print(stack.size())