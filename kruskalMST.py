class Node:
        def __init__(self,data):
                self.data = data
                self.rank = 0 
                self.parent = self

        #Return the overall Rank of current set
        def findRank(self):
                temp = self.findSet()
                return temp.rank
    
        #Find the main representative set of current set
        def findSet(self):
                temp = self.parent
                while temp.parent != temp:
                        temp = temp.parent
                #Path Compression, set the parent of current pointer to the representative set directly
                self.parent = temp
                return temp

        #Print the current hierarchy of current set, bottom's up
        def printSet(self):
                temp = self
                while 1:
                        print temp.data,
                        if temp.parent == temp:
                                break
                        temp = temp.parent
#Make a new set
def makeSet(data):
        return Node(data)

#Merge two sets
def union(set1,set2):
        #If the rank of both the sets is same, then
        if set1.findRank() == set2.findRank():
                #Set the parent of representative of set2 to representative of set1
                set2.findSet().parent = set1.findSet()
                #Increment the overall rank of set1 by 1
                set1.findSet().rank += 1
        elif set1.findRank() > set2.findRank():
                #Set the parent of representative of set2 to representative of set1
                set2.findSet().parent = set1.findSet()
        else:
                #Set the parent of representative of set1 to representative of set2
                set1.findSet().parent = set2.findSet()

class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = []

	def addEdge(self,u,v,weight):
		self.graph.append([u,v,weight])
	
	def sortedEdges(self):
		self.graph = sorted(self.graph, key=lambda item: item[2]) 
		return

def mst02(n, graph):
	lookup = {}
	for i in range(1,n+1):
		lookup[i] = makeSet(i)
	
	graph.sortedEdges()
	overallwt = 0
		
	last = 10**6
	for edge in graph.graph:
		if lookup[edge[0]].findSet()==lookup[edge[1]].findSet():
			continue
		else:
			overallwt += edge[2]
			union(lookup[edge[0]],lookup[edge[1]])
	return overallwt

f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/kruskalTestCase.txt",'r')
if __name__ == "__main__":
    n, m = f1.readline().strip().split(' ')
    n, m = [int(n), int(m)]
    graph = Graph(n)
    for edges_i in xrange(m):
        x,y,r = map(int,f1.readline().strip().split(' '))
        graph.addEdge(x,y,r)
    result = mst02(n, graph)
    print result

"""
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    graph = Graph(n)
    for edges_i in xrange(m):
        x,y,r = map(int,raw_input().strip().split(' '))
        graph.addEdge(x,y,r)
    result = mst02(n, graph)
    print result
"""
