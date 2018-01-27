from collections import defaultdict

class Graph:
	def __init__(self,vertices,data):
		self.vertices = vertices
		self.data = data
		self.totSum = sum(data)
		self.graph = defaultdict(set)

	def addEdge(self,edge):
		u = edge[0]
		v = edge[1]
		self.graph[v].add(u)
		self.graph[u].add(v)

def cutTheTreeUtil(graph,v,visited,mini):
	#print v,
	visited.add(v)

	curSum = graph.data[v-1]
		
	for i in graph.graph[v]:
		if i not in visited:
			curSum += cutTheTreeUtil(graph,i,visited,mini)
	mini[0] = min(mini[0],abs((graph.totSum-curSum)-curSum))
	return curSum

def cutTheTree(graph):
	visited = set()
	mini = [10**8]
	cutTheTreeUtil(graph,1,visited,mini)
	return mini[0]

def cutTheTree02(graph):
	visited = set()
	stack,path = [1],[]
	children = defaultdict(set)

	while stack:
		v = stack.pop()
		visited.add(v)
	
		path.append(v)	
		#for i in graph.graph[v]:
		children[v] = clist = [c for c in graph.graph[v] if c not in visited]
		stack.extend(clist)
	#print children
	
	mini = 10**8

	for i in path[::-1]:
		curSum = graph.data[i-1] + sum(graph.data[c-1] for c in children[i])
		mini = min(mini, abs((graph.totSum-curSum)-curSum))
		graph.data[i-1] = curSum
	return mini

if __name__ == "__main__":
    n = int(raw_input().strip())
    data = map(int, raw_input().strip().split(' '))
    #edges = []
    graph = Graph(n,data)
    for edges_i in xrange(n-1):
        edges_temp = map(int,raw_input().strip().split(' '))
	graph.addEdge(edges_temp)
    #print graph.graph
    result = cutTheTree02(graph)
    print result
