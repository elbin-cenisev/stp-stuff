class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

q = "Type out a string that should be reversed: "
original = input(q)

stack = Stack()
for l in original:
    stack.push(l)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
