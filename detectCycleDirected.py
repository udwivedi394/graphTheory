import directedGraph as dirG
import time

def detectCycle(graph):
	vertices = graph.getVertices()
	print vertices
	recursionStack = []
	for i in range(len(vertices)):
		visited = [False]*len(vertices)
		if detectCycleUtil(vertices,i,visited,recursionStack):
			return True
		print
	return False

def detectCycleUtil(graph,v,visited,recursionStack):
	visited[v] = True
	print v,
	
	recursionStack.append(v)
	
	check=False
	for i in graph[v]:
		if visited[i]==False:
			check = detectCycleUtil(graph,i,visited,recursionStack)

		if i in recursionStack:
			return True

		if check:
			return True
	recursionStack.pop()
	return False

g1 = dirG.DirectedGraph()
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,1)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,4)

g1.printGraph()
print detectCycle(g1)
