import directedGraph as dirG

#Detects whether any cycle is present in Directed Graph,
#True->cycle present, False->cycle absent
def detectCycle(graph):
	vertices = graph.getVertices()
	
	#Keep track of visited vetices
	visited = [False]*len(vertices)
	#Keep track of the vertices in the running path, to check if any vertex falls in the running stack
	recursionStack = [False]*len(vertices)

	#To check every separate tree in the graph
	for i in range(len(vertices)):
		if visited[i]==False:
			if detectCycleUtil(vertices,i,visited,recursionStack):
				return True
	return False

#Utility to perform above operations
def detectCycleUtil(graph,v,visited,recursionStack):
	#Mark the current vertex as visited in Visited Loopkup
	visited[v] = True
	#Mark the current vertex as visited in current path
	recursionStack[v] = True
	print v,
	
	check=False
	#Iterate all the edges in the adjacency of current vertex 
	for i in graph[v]:
		#If the vertex is not already visited
		if visited[i]==False:
			check = detectCycleUtil(graph,i,visited,recursionStack)
		
		#If not visited, check if the current vertex falls in the current path
		elif recursionStack[i]==True:
			return True

		if check:
			return True

	#BackTrack, unmark the current vertex as visited in recursion stack
	recursionStack[v]=False
	return False

g1 = dirG.DirectedGraph()
g1.addEdge(0,1)
g1.addEdge(0,2)
#g1.addEdge(1,1)
g1.addEdge(1,2)
#g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(5,5)

g1.printGraph()
print "\n",detectCycle(g1)
