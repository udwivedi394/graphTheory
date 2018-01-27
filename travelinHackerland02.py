import sys
import time

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
	def __init__(self,vertices,types):
		self.vertices = vertices
		self.graph = []
		self.graphmap = {}
		self.buildingType=[None]+types

	def addEdge(self,u,v,weight):
		self.graph.append([u,v,weight])
	
	def sortedEdges(self):
		self.graph = sorted(self.graph, key=lambda item: item[2]) 
		return

def mst(n, graph,lookup,cycle_edges):
	for i in range(1,n+1):
		lookup[i] = makeSet(i)
	
	graph.sortedEdges()
	#print graph.graph
	for i in range(len(graph.graph)):
		edge = graph.graph[i]
		if graph.graphmap.get(edge[0])==None:
			graph.graphmap[edge[0]] = set()
		if graph.graphmap.get(edge[1])==None:
			graph.graphmap[edge[1]] = set()
		graph.graphmap[edge[0]].add(i)
		graph.graphmap[edge[1]].add(i)

		if lookup[edge[0]].findSet()==lookup[edge[1]].findSet():
			cycle_edges.append(i)
			continue
		else:
			union(lookup[edge[0]],lookup[edge[1]])
	return

def mst03(n, graph, s, d, k, lookup, cycle_edges):
	print "(s,d):",(s,d)
	node = s #it is the vertex or city

	#contains the edge positions
	stack = sorted(list(graph.graphmap[s]-set(cycle_edges)))[::-1]

	#to keep track of visited vertex
	visited = set()

	#to keep track of total number of visited buildings
	totVisitedType = set()
	maxi = -1
	found1 = found2 = False

	#to keep track of all the visited edges
	visitedEdge=set()

	while len(stack):
		#print stack
		cur_edge_pos = stack.pop()
		if cur_edge_pos not in visitedEdge:
			visitedEdge.add(cur_edge_pos)
		else:
			continue

		#stack.remove(cur_edge_pos)
		edge = graph.graph[cur_edge_pos]
		visited.add(node)
		print cur_edge_pos,edge
		
		maxi = max(maxi,edge[2])
		
		totVisitedType.add(graph.buildingType[edge[0]])
		totVisitedType.add(graph.buildingType[edge[1]])
		
		if d in edge[:2]:
			found1 = True
		if len(totVisitedType)>=k:
			found2 = True

		if found1 and found2:
			break

		node = edge[0] if edge[1]==node else edge[1]
		if node not in visited:
			stack += sorted(list(graph.graphmap[node]-set(cycle_edges)))[::-1]
	
	print "Maxi:",maxi
	print totVisitedType
	if found1 and found2:
		return maxi
	return -1

def mst02(n, graph, s, d, k, lookup, cycle_edges):
	current_set = lookup[s].findSet()
	maxi = -1
	totVisitedType = set()
	found1 = found2 = False

	for edge in graph.graph:
		if lookup[edge[0]].findSet()==current_set and set(edge[:2]) not in cycle_edges:
			totVisitedType.add(graph.buildingType[edge[0]])
			totVisitedType.add(graph.buildingType[edge[1]])
			
			if d in edge[:2]:
				found1 = True
			if len(totVisitedType) >= k:
				found2 = True	
			maxi = max(maxi, edge[2])
			#print edge,
	if found1 and found2:
		return maxi
	return -1
#"""
if __name__ == "__main__":
    try:
	f1 = open("travelHackerTest#1.txt",'r')
        #f2 = open("travelHackerOutput.txt",'w')

 	n,m,q = f1.readline().strip().split(' ')
    	n,m,q = [int(n),int(m),int(q)]
    	types = map(int,f1.readline().strip().split(' '))
    	graph = Graph(n,types)
    
    	for edges_i in xrange(m):
       		x,y,r = map(int,f1.readline().strip().split(' '))
        	graph.addEdge(x,y,r)
    
    	lookup = {}
    	cycle_edges = []
    	mst(n,graph,lookup,cycle_edges)
    	print graph.graphmap
	for a2 in xrange(q):
        	s,d,k = map(int,f1.readline().strip().split(' '))
   		try:
			if a2==4:
				result = mst03(n,graph,s,d,k,lookup,cycle_edges)
    				print result
				time.sleep(10)
		except Exception as e:
			print e
    finally:
	f1.close()
"""
if __name__ == "__main__":
    n,m,q = sys.stdin.readline().strip().split(' ')
    n,m,q = [int(n),int(m),int(q)]
    types = map(int,sys.stdin.readline().strip().split(' '))
    graph = Graph(n,types)
    
    for edges_i in xrange(m):
        x,y,r = map(int,sys.stdin.readline().strip().split(' '))
        graph.addEdge(x,y,r)
    
    lookup = {}
    cycle_edges = []
    mst(n,graph,lookup,cycle_edges)
    print graph.graph
    print graph.graphmap
    for a2 in xrange(q):
        s,d,k = map(int,sys.stdin.readline().strip().split(' '))
   	result = mst03(n,graph,s,d,k,lookup,cycle_edges)
    	print result
#"""
