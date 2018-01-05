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

graph = Graph(5)
graph.addEdge(0,1)
graph.addEdge(0,4)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(1,4)
graph.addEdge(2,3)
graph.addEdge(3,4)

graph.printGraph()
