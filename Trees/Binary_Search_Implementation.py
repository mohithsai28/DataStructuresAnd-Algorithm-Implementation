class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearch():
    def __init__(self):
        self.root=None
    def insert(self,data):
        newnode=node(data)
        if(self.root==None):
            self.root=newnode
            return
        else:
            currentnode=self.root
            while (True):
                if (currentnode.data > newnode.data):
                    if(currentnode.right==None):
                        currentnode.right=newnode
                        return
                    else:
                        currentnode=currentnode.right
                if (currentnode.data<newnode.data):
                        if (currentnode.left == None):
                            currentnode.left = newnode
                            return
                        else:
                            currentnode = currentnode.left
    def lookup(self,value):
        if(self.root==None):
            return False
        currentnode=self.root
        while(True):
            if currentnode==None:
                return False
            if(currentnode.data==value):
                return currentnode.data
            elif value<currentnode.data:
                currentnode=currentnode.left
            elif value>currentnode.data:
                currentnode=currentnode.right

    def printTree(self):
        if self.root!=None:
            self.traverse(self.root)

    def traverse(self,currentnode):
        if currentnode!=None:
            self.traverse(currentnode.left)
            print(str(currentnode.data))
            self.traverse(currentnode.right)












binarysearch=BinarySearch()
binarysearch.insert(2)
binarysearch.insert(4)
binarysearch.insert(3)
binarysearch.insert(5)
print(binarysearch.lookup(7))
#print(binarysearch.root)
binarysearch.printTree()

