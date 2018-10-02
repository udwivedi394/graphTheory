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

	#This method fails for large data, because of the maximum recursion depth
	def printPaths(self,start,end):
		visited = set()
		#stack = []
		return self.printPathsUtil(start,end,visited,0) #,stack)

	def printPathsUtil(self,v,end,visited,overallValue): #,stack):	
		if v==end:
			#stack.append(v)
			#print stack, overallValue
			#stack.pop()
			return overallValue
		
		#stack.append(v)
		visited.add(v)
			
		mini = 10**8
		for node in self.graph[v]:
			if node.vertex not in visited:
				if node.data > overallValue:
					val = self.printPathsUtil(node.vertex,end,visited,node.data)#,stack)
				else:
					val = self.printPathsUtil(node.vertex,end,visited,overallValue)#,stack)
				mini = min(mini,val)
		#stack.pop()
		visited.remove(v)			
		return mini

def jackGoesToRapture(N,edges):
	graph = Graph(N)
	
	for edge in edges:
		graph.addEdge(edge[0],edge[1],edge[2])
	
	#graph.printAdjacency()
	#graph.DFS(1)
	#print
	val = graph.printPaths(1,N)
	if val == 10**8:
		return "NO PATH EXISTS"
	return val


if __name__ == "__main__":
    N, E = raw_input().strip().split(' ')
    N, E = [int(N), int(E)]
    edges = []
    for edges_i in xrange(E):
        edges_temp = map(int,raw_input().strip().split(' '))
        edges.append(edges_temp)
    result = jackGoesToRapture(N, edges)
    print result
