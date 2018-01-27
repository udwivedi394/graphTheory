#!/bin/python

import sys
import time

class MapHeap:
        def __init__(self,vertices):
                self.arr = []
                self.lookup = {}
		for i in vertices:
			self.insert(i,INF)

        def insert(self,vertex,data):
                if self.lookup.get(vertex)!=None:
                        return

                self.arr.append([vertex,data])
                self.lookup[vertex] = len(self.arr)-1
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

                inp = 0
                while 1:
                    minNode = self.minHeapify(inp)
                    if inp==minNode:
                        break
                    inp = minNode    
                return delVal
            
        def minHeapify(self,k=0):
                leftNode = leftChild(self.arr,k)
                rightNode = rightChild(self.arr,k)

                minNode = k
                if leftNode and self.arr[leftNode][1] < self.arr[minNode][1]:
                        minNode = leftNode
                if rightNode and self.arr[rightNode][1] < self.arr[minNode][1]:
                        minNode = rightNode

                if minNode != k:
                        self.lookup[self.arr[k][0]] = minNode
                        self.lookup[self.arr[minNode][0]] = k

                        swap(self.arr,minNode,k)
                return minNode

        def extractMin(self):
                return self.arr[0]

        def contains(self,vertex):
                return self.lookup.get(vertex)

        def setData(self,vertex,val):
                pos = self.contains(vertex)
                if pos==None:
                        print "Vertex Not present", vertex
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
INF = 10**8

class Graph:
        def __init__(self,vertices):
                self.vertices = vertices
                self.graph = {}
		self.vDistance = {}
		self.vParent = {}
		self.nocomingback = INF

		for i in range(0,vertices):
                	self.graph[i] = {}

        def addEdge(self,u,v,data):
		value = self.graph[u].get(v)
                value = min(value,data) if value!=None else data

		self.graph[u][v]= value                
                self.graph[v][u]= value
                return
	
	def addEdges(self,edges):
		for edge in edges:
			u = edge[0]
			v = edge[1]
			data = edge[2]
			value = self.graph[u].get(v)
                	value = min(value,data) if value!=None else data

			self.graph[u][v]= value                
                	self.graph[v][u]= value
                return
			
class SPT:
	def __init__(self):
		self.vDistance = {}
		self.vParent = {}

def dijkstraShortestPath(N,graph,mapHeap,start):
        mapHeap.setData(start,0)
        vDistance = graph.vDistance
	vParent = graph.vParent

        while mapHeap.arr:
                current = mapHeap.extractMin()
                mapHeap.delete(current[0])

                vDistance[current[0]] = current[1]
		if current[0] == start:
			vParent[start] = None

                for neighbour in graph.graph[current[0]]:
                        #If vertex exists in MapHeap then returns its position
                        pos = mapHeap.contains(neighbour)
                        if pos==None:
                                continue

                        prev_data = graph.graph[current[0]][neighbour]
                        if mapHeap.arr[pos][1] > current[1]+prev_data:
				mapHeap.setData(neighbour, current[1]+prev_data)
				vParent[neighbour] = current[0]                        
        return

def checkforPath(N,graph,vertices,start,destination,discardEdge,parentStack):
	found = False
	if min(discardEdge) > graph.nocomingback:
		return "Infinity"

	#print "DiscardEdge:",discardEdge,
	if discardEdge[0] in parentStack:
		index = parentStack.index(discardEdge[0])
		#print "Index:",index
		if (index > 0) and (index < len(parentStack)-1):
			#print "Inside 01"
			if parentStack[index-1]==discardEdge[1]:
				dst = discardEdge[1]
				src = discardEdge[0]
				found = True
			elif parentStack[index+1]==discardEdge[1]:
				src = discardEdge[0]
				dst = discardEdge[1]

		elif index == 0 and parentStack[index+1]==discardEdge[1]:
			#print "Inside 02"
			dst = discardEdge[0]
			src = discardEdge[1]
			found = True
		elif index == len(parentStack)-1 and parentStack[index-1]==discardEdge[1]:
			#print "Inside 03"
			dst = discardEdge[1]
			src = discardEdge[0]
			found = True

	if found==False:
		return graph.vDistance[destination]

	vDistance = graph.vDistance
	tempHeap = MapHeap(vertices)
	#print "dest:",dst,"source:",src
	dist_u_v,u,v = shortestPath(N,graph,tempHeap,src,dst,destination,discardEdge,parentStack,vertices)
	if dist_u_v == "Infinity":
		graph.nocomingback = min(discardEdge)
		return dist_u_v
	try:
		return vDistance[u]+dist_u_v+(vDistance[destination]-vDistance[v])
	except KeyError:
		return "Infinity"

def shortestPath(N,graph,mapHeap,start,destination,orgDest,discardEdge,parentStack,vertices):
	#print "Start,Destination:",(start,destination)
        mapHeap.setData(start,0)
        vDistance = {}
	vParent = {}
	#print mapHeap.arr
	mark = parentStack.index(start)
	leftStack = set(parentStack[mark:])
	rightStack = set(parentStack[:mark])
       	#print "LeftStack:",leftStack
	#print "RightStack:",rightStack

	mainLoop = True
	specialNodes = set()
	while mapHeap.arr and vDistance.get(destination)==None and mainLoop:
                current = mapHeap.extractMin()
                mapHeap.delete(current[0])

                vDistance[current[0]] = current[1]
		if current[0] == start:
			vParent[start] = None

                for neighbour in graph.graph[current[0]]:
                        #If vertex exists in MapHeap then returns its position
			if set([current[0],neighbour])==set(discardEdge):
				continue
                        pos = mapHeap.contains(neighbour)
                        if pos==None:
                                continue
                        prev_data = graph.graph[current[0]][neighbour]
			if neighbour in rightStack:
				#destination = neighbour
				vParent[neighbour] = current[0]
                		vDistance[neighbour] = prev_data+current[1]
				specialNodes.add(neighbour)
				#internalMinDistance = 
				#mainLoop = False
				#break

                        if mapHeap.arr[pos][1] > current[1]+prev_data:#vDistance[current[0]]+prev_data:
                                mapHeap.setData(neighbour, current[1]+prev_data)#vDistance[current[0]]+prev_data)
				vParent[neighbour] = current[0]                                
	#print "NewParent:",vParent
	#print "NewDist:",vDistance
	#print "Specail Nodes:",specialNodes
	new_stack = []
	key = destination
	#new_stack_set = set()
	while key!=None:
		new_stack.append(key)
		#new_stack_set.add(key)
		key = vParent.get(key)

	#print "NewStack:",new_stack
	u = None
	v = None
	"""
	if new_stack_set&rightStack:
		pass
	else:
		#print "returning"
		return "Infinity",u,v
	"""
	while new_stack:
		top = new_stack.pop()
		if top in leftStack:
			u = top
		if v==None and top in rightStack:
			v = top
		if u and v:
			break
	v = parentStack[min(parentStack.index(node) for node in specialNodes)]
	#print "u,v:",(u,v),
	dist = dijkstraShortestPath02(N,graph,MapHeap(vertices),u,v,discardEdge)
	#print dist
	return dist, u, v
	#return vDistance[v]-vDistance[u] if vDistance.get(v)!=None and vDistance.get(u)!=None else "Infinity",u,v

def dijkstraShortestPath02(N,graph,mapHeap,start,dest,discardEdge):
        mapHeap.setData(start,0)
        vDistance = {}
	vParent = {}

        while mapHeap.arr and vDistance.get(dest)==None:
                current = mapHeap.extractMin()
                mapHeap.delete(current[0])

                vDistance[current[0]] = current[1]
		if current[0] == start:
			vParent[start] = None

                for neighbour in graph.graph[current[0]]:
			if set([current[0],neighbour])==set(discardEdge):
				continue
                        #If vertex exists in MapHeap then returns its position
                        pos = mapHeap.contains(neighbour)
                        if pos==None:
                                continue

                        prev_data = graph.graph[current[0]][neighbour]
                        if mapHeap.arr[pos][1] > current[1]+prev_data:
				mapHeap.setData(neighbour, current[1]+prev_data)
				vParent[neighbour] = current[0]                        
        return vDistance[dest]
#"""
f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/goingtoOfficeTestCase02.txt",'r')
n,m = f1.readline().strip().split(' ')
n,m = [int(n),int(m)]

graph = Graph(n)
vertices = set()

for a1 in xrange(m):
	x,y,r = f1.readline().strip().split(' ')
	x,y,r = [int(x),int(y),int(r)]
	graph.addEdge(x,y,r)
	vertices.add(x)
	vertices.add(y)
	
#print graph.graph
mapHeap = MapHeap(vertices)
originalSPT = SPT()

s,d = f1.readline().strip().split(' ')
s,d = [int(s),int(d)]
q = int(f1.readline().strip())
dijkstraShortestPath(n,graph,mapHeap,s)
#print "OrgDist:",graph.vDistance
#print "OrgParent:",graph.vParent
parentStack = []
key = d
while key!=None:
	parentStack.append(key)
	key = graph.vParent.get(key)
#print parentStack

count1 = 0
count2 = 0
for a2 in xrange(q):
	x,y = f1.readline().strip().split(' ')
	x,y = [int(x),int(y)]
	print "Edge:",(x,y)
	result = checkforPath(n,graph,vertices,s,d,[x,y],parentStack)
	print result
	#time.sleep(0.2)
	if result == 185351:
		count1 += 1
	if result == "Infinity":
		count2 += 1
print count1, count2
#"""
"""
n,m = sys.stdin.readline().strip().split(' ')
n,m = [int(n),int(m)]

graph = Graph(n)
vertices = set()

for a1 in xrange(m):
	x,y,r = sys.stdin.readline().strip().split(' ')
	x,y,r = [int(x),int(y),int(r)]
	graph.addEdge(x,y,r)
	vertices.add(x)
	vertices.add(y)
	
#print graph.graph
mapHeap = MapHeap(vertices)

s,d = sys.stdin.readline().strip().split(' ')
s,d = [int(s),int(d)]
q = int(sys.stdin.readline().strip())
dijkstraShortestPath(n,graph,mapHeap,s)
parentStack = []
key = d
while key!=None:
	parentStack.append(key)
	key = graph.vParent.get(key)
print "Parent:",parentStack

for a2 in xrange(q):
	x,y = sys.stdin.readline().strip().split(' ')
	x,y = [int(x),int(y)]
	result = checkforPath(n,graph,vertices,s,d,[x,y],parentStack)
	print result

"""
"""
f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/goingtoOfficeTestCase02.txt",'r')
n,m = f1.readline().strip().split(' ')
n,m = [int(n),int(m)]

graph = Graph(n)
vertices = set()

for a1 in xrange(m):
	x,y,r = f1.readline().strip().split(' ')
	x,y,r = [int(x),int(y),int(r)]
	graph.addEdge(x,y,r)
	vertices.add(x)
	vertices.add(y)
	
#print graph.graph
mapHeap = MapHeap(vertices)

s,d = f1.readline().strip().split(' ')
s,d = [int(s),int(d)]
q = int(raw_input().strip())
dijkstraShortestPath(n,graph,mapHeap,s)
#print "OrgDist:",graph.vDistance
#print "OrgParent:",graph.vParent
parentStack = []
key = d
while key!=None:
	parentStack.append(key)
	key = graph.vParent.get(key)
#print parentStack
#print graph.graph[0]

count1 = 0
count2 = 0
for a2 in xrange(q):
	x,y = raw_input().strip().split(' ')
	x,y = [int(x),int(y)]
	print "Edge:",(x,y)
	result = checkforPath(n,graph,vertices,s,d,[x,y],parentStack)
	print result
	time.sleep(0.2)
	if result == 185351:
		count1 += 1
	if result == "Infinity":
		count2 += 1
print count1, count2
#"""
