class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class DirectedGraph:
	def __init__(self,vertices):
		self.arr = [None]*vertices

	def addEdge(self,u,v):
		temp = self.arr[u]
		self.arr[u] = Node(v)
		self.arr[u].next = temp
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

	#Depth First Traversal
	def DFS(self,start):
		visited = [False]*len(self.arr)
		stack = []
		
		#Start from the vertex given
		node = start
		while 1:
			#Keep on visiting till the current vertex is not already visited
			while visited[node]==False:
				#Print the node
				print node,
				#Mark the current vertex as visited, and push it in stack
				visited[node]=True
				stack.append(node)
				if self.arr[node]:
					#Move to the next vertex given in adjancy
					node = self.arr[node].data

			#If the last vertex is visted and stack is not empty
			while visited[node] and len(stack):
				#Take the top of the stack as current vertex
				node = stack[-1]
				#Traverse the linkedlist attached at the head of it, and find for any unvisited vertex
				temp = self.arr[node]
				found = False
				while temp:
					if visited[temp.data]==False:
						found = True
						break
					temp = temp.next
				if found:
					#If unvisited vertex found set the node to it
					node = temp.data
				else:
					#Otherwise pop the top
					stack.pop()

			#If current vertex is already visited and stack is empty then traverse is complete
			if visited[node] and len(stack)==0:
				break
		return

	def getVertices(self):
		return self.arr
