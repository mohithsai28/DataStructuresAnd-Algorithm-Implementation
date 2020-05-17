class graph:
    def __init__(self):
        self.numberofnodes=0;
        self.adjacentList={}
    def addvertex(self,node):
        self.adjacentList[node]=[]
        self.numberofnodes+=1
    def addEdge(self,node1,node2):
        #as undirection graph we assign both nodes to each other as we can tranverse from both direction
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    def showconnections(self):
        for m,n in self.adjacentList.items():
            print(f"{m}---->{n}")

graph=graph()
graph.addvertex('0')
graph.addvertex('1')
graph.addvertex('2')
graph.addvertex('3')
graph.addvertex('4')
graph.addvertex('5')
graph.addvertex('6')
graph.addEdge('0','1')
graph.addEdge('0','2')
graph.addEdge('1','2')
graph.addEdge('1','3')
graph.addEdge('2','4')
graph.addEdge('3','4')
graph.addEdge('4','5')
graph.addEdge('5','6')
# print(graph)
graph.showconnections()

