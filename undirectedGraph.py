class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class UnDirGraph:
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
		print
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

	def DFS(self,start):
		visited = [False]*len(self.arr)
		stack = []
		node = start
		while 1:
			while visited[node]==False:
				print node,
				visited[node]=True
				stack.append(node)
				node = self.arr[node].data

			while visited[node] and len(stack):
				node = stack.pop()
				temp = self.arr[node]
				found = False
				while temp:
					if visited[temp.data]==False:
						found = True
						break
					temp = temp.next
				if found:
					node = temp.data
			if visited[node] and len(stack)==0:
				break
		return
