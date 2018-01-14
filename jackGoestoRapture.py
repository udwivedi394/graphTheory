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

	def printPaths(self,start,end):
		visited = set()
		stack = []
		self.printPathsUtil(start,end,visited,stack)

	def printPathsUtil(self,v,end,visited,stack):	
		if v==end:
			stack.append(v)
			print stack
			stack.pop()
			return
		
		stack.append(v)
		visited.add(v)		

		for node in self.graph[v]:
			if node.vertex not in visited:
				self.printPathsUtil(node.vertex,end,visited,stack)
		stack.pop()
		visited.remove(v)			
		
def jackGoesToRapture(N,edges):
	graph = Graph(N)
	
	for edge in edges:
		graph.addEdge(edge[0],edge[1],edge[2])

	graph.printAdjacency()

	graph.DFS(1)
	
	print
	graph.printPaths(1,5)


if __name__ == "__main__":
    N, E = raw_input().strip().split(' ')
    N, E = [int(N), int(E)]
    edges = []
    for edges_i in xrange(E):
        edges_temp = map(int,raw_input().strip().split(' '))
        edges.append(edges_temp)
    result = jackGoesToRapture(N, edges)
    print result
