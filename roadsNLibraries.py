import sys
class Graph:
        def __init__(self,vertices):
                self.vertices = vertices
                self.graph = {}
		self.connectedComp = {}

                for i in range(1,vertices+1):
                        self.graph[i] = set()

        def addEdge(self,u,v):
                self.graph[u].add(v)
                self.graph[v].add(u)
                return
	
	def connectedComponents(self):
		notVisited = set(xrange(1,self.vertices+1))	
		visited = set()
		while notVisited:
			stack = [notVisited.pop()]
			count = 0
			while stack:
 				current = stack.pop()
				if current not in visited:
					#print current,
					count += 1
				
				visited.add(current)
				
				for neighbour in self.graph[current]:
					if neighbour not in visited:
						stack.append(neighbour)
			#print "Not:",notVisited,"Vis:",visited
			notVisited = notVisited-visited
			if self.connectedComp.get(count)==None:
				self.connectedComp[count] = 0
			self.connectedComp[count] += 1 
			#print "New:",notVisited
		return			

def roadsAndLibraries(n, c_lib, c_road, country):
	country.connectedComponents()
	#print country.connectedComp
	cost = 0
	for i,count in country.connectedComp.iteritems():
		if i==1:
			#print "LibrarystandAlone:",i,c_lib,count*c_lib
			cost += count*c_lib
		else:
			cost += (min((i-1)*c_road+c_lib,i*c_lib))*count
	return cost

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, m, c_lib, c_road = raw_input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        country = Graph(n)
	for cities_i in xrange(m):
		x,y = map(int,raw_input().strip().split(' '))
		country.addEdge(x,y)
		#result = roadsAndLibraries(n, c_lib, c_road, cities)
		#print result
	print roadsAndLibraries(n, c_lib, c_road, country)
