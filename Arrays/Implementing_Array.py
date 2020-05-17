#push(value)---->storing a value in array
#pop()----->Removes element of last index
#delete()-----> del in python removes a perticular element based on its index value
#get(index)------>grabing data at perticular index(Most Common Operation)
#We build Arrays on top of dictionary as we have (key , value) pairs which is same as (index and values) in arrays

class array():
    def __init__(self):
        self.data={}
        self.length=0
    def push(self,value):
        self.data[self.length]=value
        self.length+=1

    def pop(self):
        lastitem=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastitem

    def get(self,index):
        return self.data[index]

    def delete(self,index):
        deleted_item=self.data[index]
        #need to write code for unshifting of indexes
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        self.length -= 1
        return deleted_item





array1=array()
array1.push(1)
array1.push(3)
array1.push(4)
array1.push(5)
print(array1.length)
print(array1.data)
print(array1.pop())
print(array1.get(1))
print(array1.delete(1))
print(array1.length)
print(array1.data)



