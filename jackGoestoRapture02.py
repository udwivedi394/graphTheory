INF = 9999999999
import mapBinaryHeap as mapB
import time

class Node:
	def __init__(self,vertex,data):
		self.vertex = vertex
		self.data = data

	def __str__(self):
		return str(self.vertex)+","+str(self.data)
class Graph:
	def __init__(self,vertices):
		self.graph = {}
		self.vertices = vertices

	def addEdge(self,u,v,data):
		if self.graph.get(u)==None:
			self.graph[u] = [Node(v,data)]
		else:
			self.graph[u].append(Node(v,data))

		if self.graph.get(v)==None:
			self.graph[v] = [Node(u,data)]
		else:
			self.graph[v].append(Node(u,data))
		return
	
	def printAdjacency(self):
		for i in range(self.vertices):
			print "\nAdjaceny list of",i,":"
			print "Head"
			if self.graph.get(i):
				for node in self.graph[i]:
					print node,"->",
				print "None"
			else:
				self.graph[i] = []
		print
		return

	def DFS(self,start):
		visited = set()
		self.DFSUtil(start,visited)

	def DFSUtil(self,v,visited):
		visited.add(v)
		print v,
		for i in self.graph[v]:
			if i.vertex not in visited:
				self.DFSUtil(i.vertex,visited)
		return

def jackGoesToRapture(N,edges):
	graph = Graph(N)

	#Each Node in MapHeap, contains data in the form of [vertex,Distance]
	mapHeap = mapB.MapHeap()

	for edge in edges:
		graph.addEdge(edge[0],edge[1],edge[2])
		mapHeap.insert(edge[0],INF)
		mapHeap.insert(edge[1],INF)
	
	mapHeap.setData(1,0)
	
	vParent = {}
	vDistance = {}

	source = 1
	while len(mapHeap.arr):
		print mapHeap.arr
		print mapHeap.lookup
		current = mapHeap.extractMin()
		print "Min Value:",current
		mapHeap.delete(current[0])
		time.sleep(0.2)

		vDistance[current[0]] = current[1]
		if current[0]==source:
			vParent[current[0]] = None

		for neighbour in graph.graph[current[0]]:
			#If vertex exists in MapHeap then returns its position
			print "Neighbour of",current[0],":",neighbour,
			pos = mapHeap.contains(neighbour.vertex)
			if pos==None:
				continue
			print "pos:",pos,mapHeap.arr,mapHeap.lookup	
			print "HeapValue:",mapHeap.arr[pos][1],"New Distance:",vDistance[current[0]]+neighbour.data
			if mapHeap.arr[pos][1] > vDistance[current[0]]+neighbour.data:
				mapHeap.setData(neighbour.vertex, vDistance[current[0]]+neighbour.data)
				vParent[neighbour.vertex] = current[0]

	print vParent
	print vDistance

if __name__ == "__main__":
    N, E = raw_input().strip().split(' ')
    N, E = [int(N), int(E)]
    edges = []
    for edges_i in xrange(E):
        edges_temp = map(int,raw_input().strip().split(' '))
        edges.append(edges_temp)
    result = jackGoesToRapture(N, edges)
    print result
