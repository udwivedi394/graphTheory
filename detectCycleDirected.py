import directedGraph as dirG

def detectCycle(graph):
	stack = []
	vertices = graph.getVertices()
	node = 0
	visited = [False]*len(vertices)
	recursionStack = []

	noloop = True
	while noloop:
		while visited[node]==False:
			print node,
			visited[node]=True

			stack.append(node)
			if vertices[node]:
				node = vertices[node].data
			
			print "InLoop:",recursionStack
			if vertices[node] and node in recursionStack:
				noloop = False
				break
			else:
				recursionStack.append(node)
			
		
		while visited[node] and len(stack) and noloop:
			node = stack[-1]
			temp = vertices[node]
			found = False
			while temp:
				if visited[temp.data]==False:
					found=True
					break
				#if temp.data in recursionStack:
				#	noloop = False
					break
				temp = temp.next
			if found:
				node = temp.data
			else:
				stack.pop()

		if visited[node] and len(stack)==0:
			break

	print recursionStack
	print not noloop
	return not noloop

def DFS(graph):
	vertices = graph.getVertices()
	visited = [False]*len(vertices)
	DFSUtil(vertices,0,visited)

def DFSUtil(graph,cur_vertex,visited):
	done = True
	while done:
		if visited[cur_vertex]==False:
			print cur_vertex,
			visited[cur_vertex]=True
		
		if graph[cur_vertex]:
			DFSUtil(graph,graph[cur_vertex].data,visited)

		temp = graph[cur_vertex]
		found = False
		while temp:
			if visited[temp.data]==False:
				found = True
				cur_vertex = temp.data
				break
			temp = temp.next
		if found==False:
			done = False
	return

g1 = dirG.DirectedGraph(5)
#g1.addEdge(0,1)
g1.addEdge(0,2)
#g1.addEdge(1,1)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,4)

g1.printGraph()
#detectCycle(g1)
DFS(g1)
