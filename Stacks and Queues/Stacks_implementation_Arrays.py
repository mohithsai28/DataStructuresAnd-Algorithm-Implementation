class stacks():
    def __init__(self):
        self.array=[]
    def peek(self):
        return self.array[len(self.array)-1]
    def push(self,data):
        self.array.append(data)
        return self.array
    def pop(self):
        return self.array.pop()

stack=stacks()
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.peek())
