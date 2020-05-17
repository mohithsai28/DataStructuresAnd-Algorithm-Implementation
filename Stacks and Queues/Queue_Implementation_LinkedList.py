#Linkedlist is best for implementing Queues as we need not do unshifting as in arrays after deleting which is O(n).

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Queues():
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0
    def peek(self):
        return self.first.data
    def push(self,data):
        newnode=Node(data)
        if self.length==0:
            self.first=newnode
            self.last=newnode
        else:

            self.last.next=newnode
            self.last=newnode
        self.length+=1

    def pop(self):
        if self.first==self.last:
            self.first=None
            self.last = None
            return None
        else:
            temp=self.first
            self.first=temp.next
            self.length-=1
            return temp.data
    def printlist(self):
        while(self.first!=None):
            print(self.first.data, end=' ')
            self.first=self.first.next
        print()
        print(self.length)



queues=Queues()
queues.push(1)
queues.push(2)
queues.push(3)
queues.push(4)
#print(queues.peek())
queues.pop()
queues.pop()
queues.pop()
print(queues.pop())
# print(queues.first.data)
# print(queues.last.data)
queues.printlist()