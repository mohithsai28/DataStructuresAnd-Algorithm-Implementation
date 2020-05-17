class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearch():
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = node(data)
        if (self.root == None):
            self.root = newnode
            return
        else:
            currentnode = self.root
            while (True):
                if (currentnode.data > newnode.data):
                    if (currentnode.right == None):
                        currentnode.right = newnode
                        return
                    else:
                        currentnode = currentnode.right
                if (currentnode.data < newnode.data):
                    if (currentnode.left == None):
                        currentnode.left = newnode
                        return
                    else:
                        currentnode = currentnode.left

    def lookup(self, value):
        if (self.root == None):
            return False
        currentnode = self.root
        while (True):
            if currentnode == None:
                return False
            if (currentnode.data == value):
                return currentnode.data
            elif value < currentnode.data:
                currentnode = currentnode.left
            elif value > currentnode.data:
                currentnode = currentnode.right

    def printTree(self):
        if self.root != None:
            self.traverse(self.root)

    def traverse(self, currentnode):
        if currentnode != None:
            self.traverse(currentnode.left)
            print(str(currentnode.data))
            self.traverse(currentnode.right)



    def depthfirstsearch_inorder(self,curr_node,list):
        if curr_node!=None:
            if curr_node.right!=None:
                self.depthfirstsearch_inorder(curr_node.right,list)
            list.append(curr_node.data)
            if curr_node.left!=None:
                self.depthfirstsearch_inorder(curr_node.left,list)
        return list

    def depthfirstsearch_preorder(self, curr_node, list):
        if curr_node != None:
            list.append(curr_node.data)
            if curr_node.right != None:
                self.depthfirstsearch_preorder(curr_node.right, list)

            if curr_node.left != None:
                self.depthfirstsearch_preorder(curr_node.left, list)
        return list

    def depthfirstsearch_postorder(self, curr_node, list):
        if curr_node != None:

            if curr_node.right != None:
                self.depthfirstsearch_postorder(curr_node.right, list)

            if curr_node.left != None:
                self.depthfirstsearch_postorder(curr_node.left, list)
            list.append(curr_node.data)
        return list



binarysearch = BinarySearch()
binarysearch.insert(2)
binarysearch.insert(4)
binarysearch.insert(3)
binarysearch.insert(5)
#print(binarysearch.breadthfirstsearch())
#print(binarysearch.breadthfirstsearchrecursive([binarysearch.root], []))
print(binarysearch.depthfirstsearch_inorder(binarysearch.root, []))
print(binarysearch.depthfirstsearch_preorder(binarysearch.root, []))
print(binarysearch.depthfirstsearch_postorder(binarysearch.root, []))
# print(binarysearch.lookup(7))
# print(binarysearch.root)
binarysearch.printTree()


