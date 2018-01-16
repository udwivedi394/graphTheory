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
		self.graph[u].append(Node(v,data))
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

def jackGoesToRapture(N,graph,mapHeap):
	mapHeap.setData(1,0)
	
	vDistance = {}
	
	minimumCost = INF
	while len(mapHeap.arr):
		current = mapHeap.extractMin()
		mapHeap.delete(current[0])

		vDistance[current[0]] = current[1]

		for neighbour in graph.graph[current[0]]:
			#If vertex exists in MapHeap then returns its position
			pos = mapHeap.contains(neighbour.vertex)
			if pos==None:
				continue
			if mapHeap.arr[pos][1] > max(vDistance[current[0]],neighbour.data):
				if neighbour.vertex == N:
					minimumCost = min(minimumCost,max(vDistance[current[0]],neighbour.data))
				mapHeap.setData(neighbour.vertex, max(vDistance[current[0]],neighbour.data))

	if minimumCost!=INF:
		print minimumCost
	else:
		print "NO PATH EXISTS"

if __name__ == "__main__":
    N, E = raw_input().strip().split(' ')
    N, E = [int(N), int(E)]
    graph = Graph(N)
    mapHeap = mapB.MapHeap()
    for edges_i in xrange(E):
        x,y,r = map(int,raw_input().strip().split(' '))
	graph.addEdge(x,y,r)
	mapHeap.insert(x,INF)
	mapHeap.insert(y,INF)
    jackGoesToRapture(N,graph,mapHeap)
