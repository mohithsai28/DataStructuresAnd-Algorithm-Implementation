# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = self.head
#             self.length = 1
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             self.length += 1
#
#     def printList(self):
#         while self.head != None:
#             print(self.head.data, end=' ')
#             self.head = self.head.next
#         print()
#         print('Length = '+ str(self.length))
#
#     def prepend(self,data):
#         new_node = Node(data)
#         current_head = self.head
#         self.head = new_node
#         self.head.next = current_head
#         self.length += 1
#
#     def insert(self, index, data):
#         if index == 0:
#             self.prepend(data)
#             return
#
#         if index > self.length-1:
#             self.append(data)
#             return
#
#         i=0
#         new_node = Node(data)
#         temp = self.head
#
#         while i<self.length:
#             if i == index-1:
#                 new_node.next = temp.next
#                 temp.next = new_node
#                 self.length+=1
#                 break
#             temp = temp.next
#             i+=1
#
#     def remove(self,index):
#         i=0
#         temp = self.head
#
#         while i < self.length:
#             if index == 0:
#                 self.head = temp.next
                self.length -=1
                break

            # last element can also be deleted by this, but have to set tail
            if i==index-1:
                to_delete = temp.next
                temp.next = to_delete.next
                if index == self.length-1:
                    self.tail = temp
                self.length -=1
                break
            i+=1
            temp = temp.next

    def reverse(self):
        if self.length == 1:
            return self.head

        leader = self.head
        self.tail= self.head
        second = leader.next
        while second != None:
            third = second.next
            second.next = leader
            leader = second
            second = third

        self.head.next = None
        self.head = leader

if __name__ == "__main__":
    li = LinkedList()
    li.append(50)
    li.append(40)
    li.append(30)
    li.append(10)
    li.insert(0,99)
    li.insert(57, 44)
    li.insert(4, 20)
    li.remove(6)
    print(li.head.data, li.tail.data)
    li.printList()
# 
# 
# obj1={'a':'hello'}
# obj2=obj1
print(obj2[a])