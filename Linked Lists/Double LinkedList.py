#5--->10--->15
#5(next={'value':10,Next:'None'})
#value=10
#next={'value':10,Next:'None'}
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublelinkedlist():
    def __init__(self):
        self.head=None
        self.tail=self.head

    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            self.length=1
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
            self.length+=1
    def prepend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            length=1
        else:
            #self.tail=self.head
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            #self.head=newnode
            self.length+=1

    def insert(self,index,value):
        newnode=Node(value)
        self.temp=self.head

        i=0
        while(i<=self.length):
            if index == 0:
                self.prepend(value)
                break
            if index == self.length:
                self.append(value)
                break
            if i==index-1:
                newnode.next=self.temp.next
                self.temp.next=newnode
                newnode.prev=self.temp
                self.length += 1
                break
            self.temp=self.temp.next
            i+=1

    def delete(self,index):
        i=0
        print(self.head.data)
        todeletebefore=self.head
        while(i<=self.length):
            # last element can also be deleted by this, but have to set tail
            if index==0:
                self.head=todeletebefore.next
                break

            if i==index-1:
                print(i)
                todeletenext = todeletebefore.next
                todeletebefore.next=todeletenext.next
                todeletenext.prev =todeletebefore
                if index == self.length-1:
                    self.tail = todeletebefore


                break
            todeletebefore=todeletebefore.next

            i+=1
        self.length-=1

    def reverse(self):
        if self.length == 1:
            return self.head
        leader=self.head
        self.tail=self.head
        second=leader.next
        while(second!=None):
            third=second.next
            second.next=leader
            leader = second
            second=third
        self.head.next=None
        self.head=leader



    def printlist(self):
        while self.head!=None:
            print(self.head.data, end=' ')
            self.head=self.head.next
        print()
        print("length is " + str(self.length))

linked=Doublelinkedlist()
linked.append(10)
linked.append(20)
linked.append(25)
linked.prepend(5)
linked.insert(4,30)
#5 10 20 25 30
linked.delete(4)
#print(linked.head)
#linked.delete(2)
#linked.delete(3)
linked.reverse()

print(linked.printlist())



