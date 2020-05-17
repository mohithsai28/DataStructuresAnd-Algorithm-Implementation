class hashtable:
    def __init__(self):
        self.array=[None]*50
        self.addresslist=[]
        self.keys=[]
        self.add=-1
    def _hash(self):
        self.add+=1
        return self.add
    def set(self,keys,values):
        address=self._hash()
        self.array[address]=[keys,values]
        self.addresslist.append(address)
        return None
    def get(self,key):
        i=0
        while self.array[i]!=None:
            if self.array[i][0]==key:
                return self.array[i][1]
            i+=1
    def keyslist(self):
        i=0
        while self.array[i]!=None:
            self.keys.append(self.array[i][0])
            i+=1
        return self.keys






hash=hashtable()
hash.set('Mohith',7)
hash.set('Rupika',1)
print(hash.get('Mohith'))
print(hash.keyslist())

