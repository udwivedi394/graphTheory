import directedGraph as dirG

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
