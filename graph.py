class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Graph:
	def __init__(self,vertices):
		self.arr = [None]*vertices

	def addEdge(self,u,v):
		temp = self.arr[u]
		self.arr[u] = Node(v)
		self.arr[u].next = temp

		temp2 = self.arr[v]
		self.arr[v] = Node(u)
		self.arr[v].next = temp2
		return

	def printGraph(self):
		for i in range(len(self.arr)):
			print "Adjacency list of vertex",i
			print "Head",
			temp = self.arr[i]
			while temp:
				print "->",temp.data,
				temp = temp.next
			print
		return
	
	#Prints the Bread First Traversal for a Graph
	def BFS(self,start):
		visited = [False]*len(self.arr)
		queue = [start]

		while len(queue):
			n = len(queue)
			while n:
				temp = queue.pop(0)
				if visited[temp] == True:
					n -= 1
					continue
			
				print temp,
				visited[temp] = True
				node = self.arr[temp]
				while node:
					queue.append(node.data)
					node = node.next
				n -= 1
		print
		return

graph1 = Graph(5)
graph1.addEdge(0,1)
graph1.addEdge(0,4)
graph1.addEdge(1,2)
graph1.addEdge(1,3)
graph1.addEdge(1,4)
graph1.addEdge(2,3)
graph1.addEdge(3,4)

graph1.printGraph()

graph1.BFS(0)


graph2 = Graph(4)
graph2.addEdge(0,1)
graph2.addEdge(0,2)
graph2.addEdge(1,2)
graph2.addEdge(2,0)
graph2.addEdge(2,3)
graph2.addEdge(3,3)

graph2.BFS(2)

g3 = Graph(7)
g3.addEdge(1,3)
g3.addEdge(1,2)
g3.addEdge(2,5)
g3.addEdge(2,4)
g3.addEdge(3,5)
g3.addEdge(4,6)
g3.addEdge(4,5)
g3.addEdge(5,6)

g3.BFS(1)
