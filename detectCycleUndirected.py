import disjointSet as disSet
import undirectedGraph as undirG

#Detect the cycle in undirected graph with help of disjoint set, using union by rank and path compression
def detectCycleUndirected(graph):
	vertices = graph.getVertices()

	lookup = {}
	for i in vertices:
		lookup[i]=disSet.makeSet(i)

	#Records all visted edges
	edges = []
	#Go through each edge
	for u in vertices:
		for v in vertices[u]:
			#If current edges is already visited
			if set([u,v]) in edges:
				continue
			#Append the current edge in edges
			edges.append(set([u,v]))

			#If the findSet of u is same as findSet of v
			#It implies there is some other way to reach here
			if lookup[u].findSet()==lookup[v].findSet():
				print "There is cycle"
				return True
			else:
				disSet.union(lookup[u],lookup[v])
	print "No Cycle"
	return False

def detectCycleDFS(graph):
	vertices = graph.getVertices()
	#Create set of visited vertices
	visitedSet = set([])
	
	#Start search from 0
	return detectCycleDFSUtil(vertices,0,0,visitedSet)

def detectCycleDFSUtil(graph,v,parent,visitedSet):
	#If current vertex is present in VistedSet, then there is cycle
	if v in visitedSet:
		return True

	#Add the current vertex in the visited set
	visitedSet.add(v)
	check = False
	#Iterate through all the adjacent edges
	for i in graph[v]:
		#Dont go in the direction of parent
		if i != parent:
			check = detectCycleDFSUtil(graph,i,v,visitedSet)
		if check:
			return True
	return False

g1 = undirG.UnDirGraph(6)
g1.addEdge(0,1)
g1.addEdge(0,5)
g1.addEdge(1,2)
g1.addEdge(1,4)
g1.addEdge(2,3)
g1.addEdge(3,4)

g1.printGraph()
detectCycleUndirected(g1)
print detectCycleDFS(g1)
