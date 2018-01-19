class Graph:
	def __init__(self,N):
		self.vertex = N
		self.graph = {}
		for i in range(1,N+1):
			self.graph[i] = set()
		return

	def addEdge(self,u,v):
		self.graph[u].add(v)
		self.graph[v].add(u)

def DFS(graph,source,guesses):
	stack = [source]
	visited = set()
	count = 0
	while stack:
		current = stack.pop()
		visited.add(current)
		#print current,

		for neighbor in graph.graph[current]:
			if neighbor not in visited:
				stack.append(neighbor)
				count += (current,neighbor) in guesses
	return count

def gcd(a,b):
	if a==0:
		return b
	return gcd(b%a,a)

def gameCount02(N,graph,guesses,g,k):
	num = 0
	den = N
	cur_count = DFS(graph,source,guesses)
	
	div = gcd(num,den)
	print "%d/%d"%(num/div,den/div)
	return

def gameCount(N,graph,guesses,g,k):
	num = 0
	den = N
	for source in range(1,N+1):
		#print source,":",
		cur_count = DFS(graph,source,guesses)
		#print "source:",source,"cur_count:",cur_count,"g:",g
		if cur_count >= k:
			num += 1
	div = gcd(num,den)
	print "%d/%d"%(num/div,den/div)
	return

f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/storyofTreeTestCase.txt",'r')

q = int(f1.readline().strip())
for a0 in xrange(q):
    n = int(f1.readline().strip())
    graph = Graph(n)
    for a1 in xrange(n-1):
        u,v = f1.readline().strip().split(' ')
        u,v = [int(u),int(v)]
        graph.addEdge(u,v)
        
    g,k = f1.readline().strip().split(' ')
    g,k = [int(g),int(k)]
    guesses = set()
    for a1 in xrange(g):
        u,v = f1.readline().strip().split(' ')
        u,v = [int(u),int(v)]
        guesses.add((u,v))
    gameCount(n,graph,guesses,g,k)

"""
q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    graph = Graph(n)
    for a1 in xrange(n-1):
        u,v = raw_input().strip().split(' ')
        u,v = [int(u),int(v)]
        graph.addEdge(u,v)
        
    g,k = raw_input().strip().split(' ')
    g,k = [int(g),int(k)]
    guesses = {}
    for a1 in xrange(g):
        u,v = raw_input().strip().split(' ')
        u,v = [int(u),int(v)]
        if guesses.get(u)==None:
            guesses[u] = set()
        guesses[u].add(v)
    gameCount(n,graph,guesses,g)
"""
