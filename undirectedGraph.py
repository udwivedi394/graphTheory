class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class UnDirGraph:
	def __init__(self,vertices):
		self.graph = {}
		self.vertices = vertices
		for i in range(self.vertices):
			self.graph[i]=[]

	def addEdge(self,u,v):
		if self.graph.get(u):
			self.graph[u].append(v)
		else:
			self.graph[u] = [v]

		if self.graph.get(v):
			self.graph[v].append(u)
		else:
			self.graph[v] = [u]
		return

	def printGraph(self):
		for i in range(self.vertices):
			print "\nAdjacency list of vertex",i
			print "Head",
			if self.graph.get(i):
				print self.graph[i],
			else:
				self.graph[i] = []
		print
		return
	
	#Prints the Bread First Traversal for a Graph
	def BFS(self,start):
		visited = [False]*len(self.graph)
		queue = [start]
		
		print self.graph
		while len(queue):
			n = len(queue)
			while n:
				temp = queue.pop(0)
				if visited[temp] == True:
					n -= 1
					continue
			
				print temp,
				visited[temp] = True
				for i in self.graph[temp]:
					queue.append(i)
				n -= 1
		print
		return
	
	def DFS(self,start):
		visited = [False]*len(self.graph)
		self.DFSUtil(start,visited)

	def DFSUtil(self,v,visited):
		visited[v] = True
		print v,
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i,visited)
		return

	def getVertices(self):
		return self.graph
