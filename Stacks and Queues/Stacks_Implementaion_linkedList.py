#stacks implementaion using linked list(ity can be done using arrays or linked list)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class stacks():
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0

    def peek(self):
        return self.top

    def push(self,data):
        newnode=Node(data)
        #print(newnode.data)
        #print(self.length)
        if self.length==0:
            self.top=newnode
            self.bottom=newnode
            self.length+=1
        else:
            newnode.next=self.top
            self.top=newnode
            self.length+=1

    def pop(self):
        if(self.top==None):
            return None
        if self.top==self.bottom:
            self.bottom=None
        temp=self.top
        self.top=self.top.next
        self.length-=1
        return temp


    def printlist(self):
        while(self.top!=None):
            print(self.top.data, end=' ')
            self.top=self.top.next
        print()
        print(self.length)

stacks=stacks()
#print(stacks.peek())
stacks.push(1)
stacks.push(2)
stacks.push(3)
# stacks.pop()
# stacks.pop()
# stacks.pop()
print(stacks.top.data)
print(stacks.bottom.data)
stacks.printlist()





