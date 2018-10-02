class MapHeap:
	def __init__(self):
		self.arr = []
		self.lookup = {}

	def insert(self,vertex,data):
		if self.lookup.get(vertex)!=None:
			return

		self.arr.append([vertex,data])
		i = len(self.arr)-1
		self.lookup[vertex] = i

		while self.arr[i][1] < parent(self.arr,i,1):
			val = self.lookup[vertex] = parent(self.arr,i)
			self.lookup[self.arr[val][0]] = i
			swap(self.arr,i,parent(self.arr,i))
			i = parent(self.arr,i)
		return

	def delete(self,vertex):
		i = len(self.arr)-1
		key_to_delete = self.lookup.get(vertex)
		if key_to_delete==None:
			return None

		self.lookup[self.arr[i][0]] = key_to_delete
		self.lookup[self.arr[key_to_delete][0]] = i
		swap(self.arr,i,key_to_delete)
		
		delVal = self.arr.pop()
		self.lookup.pop(vertex)

		self.minHeapify()
		return delVal

	def minHeapify(self,k=0):
		leftNode = leftChild(self.arr,k)
		rightNode = rightChild(self.arr,k)

		#print "Heapify",leftNode,rightNode
		minNode = k
		if leftNode and self.arr[leftNode][1] < self.arr[minNode][1]:
			minNode = leftNode
		if rightNode and self.arr[rightNode][1] < self.arr[minNode][1]:
			minNode = rightNode

		if minNode != k:
			self.lookup[self.arr[k][0]] = minNode
			self.lookup[self.arr[minNode][0]] = k

			swap(self.arr,minNode,k)
			self.minHeapify(minNode)
		return

	def extractMin(self):
		return self.arr[0]
	
	def contains(self,vertex):
		return self.lookup.get(vertex)

	def addData(self,vertex,val):
		pos = self.contains(vertex)
		if pos==None:
			print "Vertex Not present"
			return None
		self.arr[pos][1] += val
		self.minHeapify()

	def setData(self,vertex,val):
		pos = self.contains(vertex)
		if pos==None:
			print "Vertex Not present"
			return None
		self.arr[pos][1] = val
		while self.arr[pos][1] < parent(self.arr,pos,1):
			val = self.lookup[vertex] = parent(self.arr,pos)
			self.lookup[self.arr[val][0]] = pos
			swap(self.arr,pos,parent(self.arr,pos))
			pos = parent(self.arr,pos)


def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp

def parent(arr,i,val=0):
	if val!=0:
		if i!=0:
			return arr[(i-1)/2][1]
		else:
			return None
	else:	
		if i!=0:
			return (i-1)/2
		else:
			return None

def leftChild(arr,i,val=0):
	if val:
		if 2*(i+1)-1 < len(arr):
			return arr[2*(i+1)-1][1]
		return None
	else:	
		if 2*(i+1)-1 < len(arr):
			return 2*(i+1)-1
		return None

def rightChild(arr,i,val=0):
	if val:
		if 2*(i+1) < len(arr):
			return arr[2*(i+1)][1]
		return None
	else:	
		if 2*(i+1) < len(arr):
			return 2*(i+1)
		return None
"""
mHeap = MapHeap()
a = 1
for i in range(50,40,-1):
	mHeap.insert(a,i)
	a += 1

print mHeap.arr, mHeap.lookup
print mHeap.delete(10)
mHeap.decreaseData(3,100)
print mHeap.arr, mHeap.lookup
"""
