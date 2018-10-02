class DirectedGraph:
	def __init__(self):
		self.graph = {}

	def addEdge(self,u,v):
		if self.graph.get(u):
			self.graph[u].append(v)
		else:
			self.graph[u] = [v]

		if self.graph.get(v)==None:
			self.graph[v] = []
		return

	def printGraph(self):
		print
		for i in range(len(self.graph)):
			print "Adjacency list of vertex",i
			print "Head:",
			if self.graph.get(i):
				print self.graph[i]
			else:
				self.graph[i] = []
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
