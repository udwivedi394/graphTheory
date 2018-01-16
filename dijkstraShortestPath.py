import mapBinaryHeap as mapB
INF = 10**8

class Node:
	def __init__(self,vertex,data):
		self.vertex = vertex
		self.data = data

	def __str__(self):
		return str(self.vertex)+","+str(self.data)
class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = {}
		for i in range(1,vertices+1):
			self.graph[i]=[]

	def addEdge(self,u,v,data):
		#if self.graph.get(u)==None:
		#	self.graph[u] = [Node(v,data)]
		#else:
		self.graph[u].append(Node(v,data))

		#if self.graph.get(v)==None:
		#	self.graph[v] = [Node(u,data)]
		#else:
		self.graph[v].append(Node(u,data))
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

def dijkstraShortestPath(N,graph,mapHeap,start):
	"""
	graph = Graph(N)
	#Each Node in MapHeap, contains data in the form of [vertex,Distance]
	mapHeap = mapB.MapHeap()

	for edge in edges:
		graph.addEdge(edge[0],edge[1],edge[2])
		mapHeap.insert(edge[0],INF)
		mapHeap.insert(edge[1],INF)
	"""
	mapHeap.setData(start,0)
	
	#vParent = {}
	vDistance = {}

	source = start
	while len(mapHeap.arr):
		current = mapHeap.extractMin()
		mapHeap.delete(current[0])

		vDistance[current[0]] = current[1]
		#if current[0]==source:
		#	vParent[current[0]] = None

		for neighbour in graph.graph[current[0]]:
			#If vertex exists in MapHeap then returns its position
			pos = mapHeap.contains(neighbour.vertex)
			if pos==None:
				continue
			if mapHeap.arr[pos][1] > vDistance[current[0]]+neighbour.data:
				mapHeap.setData(neighbour.vertex, vDistance[current[0]]+neighbour.data)
				#vParent[neighbour.vertex] = current[0]

	#print vParent
	#print vDistance
	for i in range(1,N+1):
		if i!=source:
			print vDistance[i], #if vDistance[i]!=INF else -1,
	return

"""
t = int(raw_input().strip())
for a0 in xrange(t):
	n,m = raw_input().strip().split(' ')
	n,m = [int(n),int(m)]
	edges = []
	for a1 in xrange(m):
		x,y,r = raw_input().strip().split(' ')
		x,y,r = [int(x),int(y),int(r)]
		edges.append([x,y,r])
	s = int(raw_input().strip())
	dijkstraShortestPath(n,edges,s)
	print
"""
#Take input from file
f1 = open("/home/utkarsh/Documents/dijkstraShortestPathTestcase02.txt",'r')

t = int(f1.readline().strip())
for a0 in xrange(t):
	n,m = f1.readline().strip().split(' ')
	n,m = [int(n),int(m)]
	graph = Graph(n)
	mapHeap = mapB.MapHeap()
	for a1 in xrange(m):
		x,y,r = f1.readline().strip().split(' ')
		x,y,r = [int(x),int(y),int(r)]
		graph.addEdge(x,y,r)
		mapHeap.insert(x,INF)
		mapHeap.insert(y,INF)
	s = int(f1.readline().strip())
	dijkstraShortestPath(n,graph,mapHeap,s)
f1.close()
