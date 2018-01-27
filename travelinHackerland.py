#!/bin/python

import sys
import time

class MapHeap:
        def __init__(self,arr=None,lookup=None):
                self.arr = list(arr) if arr else []
                self.lookup = dict(lookup) if lookup else {}
	
	def __del__(self):
		#print "Deleted"
		pass

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
                        #print "Vertex Not present"
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
INF = 10**12

class Graph:
        def __init__(self,vertices,types):
                self.vertices = vertices
                self.graph = {}
		self.buildingType=[None]+types
		for i in range(1,vertices+1):
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
			
            
def dijkstraShortestPath(N,graph,mapHeap,start,dest,k):
        mapHeap.setData(start,0)
        vDistance = {}
	totVisitedType = set()
	maxi = -1
	found1 = found2 = False
	vParent = {}

        while mapHeap.arr: #and len(totVisitedType)!=k:
                current = mapHeap.extractMin()
                mapHeap.delete(current[0])
		if current[1] >= INF:
			break

                vDistance[current[0]] = current[1]
		if current[0]==start:
			vParent[current[0]]=None

		totVisitedType.add(graph.buildingType[current[0]])
		if maxi < INF:
			maxi = max(current[1],maxi)

		if current[0] == dest:
			found1 = True
		if len(totVisitedType) >= k:
			found2 = True
		
		if found1 and found2:
			break

                for neighbour in graph.graph[current[0]]:
                        #If vertex exists in MapHeap then returns its position
                        pos = mapHeap.contains(neighbour)
                        if pos==None:
                                continue
                        prev_data = graph.graph[current[0]][neighbour]
                        if mapHeap.arr[pos][1] > max(current[1],prev_data):#vDistance[current[0]]+prev_data:
                                mapHeap.setData(neighbour, max(current[1],prev_data))#vDistance[current[0]]+prev_data)
				vParent[neighbour] = current[0]
        if start==621 and dest==291:
		parentStack = []
		key = d 
		while key!=None:
			parentStack.append(key)
			key = vParent.get(key)
		print parentStack

	if found1 and found2:
		return maxi
	return -1

if __name__ == "__main__":
	try:
	    f1 = open("travelHackerTest#1.txt",'r')
	    f2 = open("travelHackerOutput.txt",'w')
	    n,m,q = f1.readline().strip().split(' ')
	    n,m,q = [int(n),int(m),int(q)]
	    types = map(int,f1.readline().strip().split(' '))
	    graph = Graph(n,types)
	    vertices = set()
	    for a1 in xrange(m):
	        x,y,r = f1.readline().strip().split(' ')
	        x,y,r = [int(x),int(y),int(r)]
	        graph.addEdge(x,y,r)
		vertices.add(x)
		vertices.add(y)

	    t1 = time.time()
	    for a2 in xrange(q):
	    	s,d,k = map(int,f1.readline().strip().split(' '))
	    	mapHeap = MapHeap()
	    	for i in vertices:
	     		mapHeap.insert(i,INF)
	    	result = dijkstraShortestPath(n,graph,mapHeap,s,d,k)
		if a2==4:
			print result
			time.sleep(10)
		f2.write(str(result)+'\n')
		del mapHeap
	    t2 = time.time()
	except Exception as e:
		print e
	finally:
		f1.close()
		f2.close()
		print "Time:",t2-t1
"""
if __name__ == "__main__":
    n,m,q = raw_input().strip().split(' ')
    n,m,q = [int(n),int(m),int(q)]
    types = map(int,sys.stdin.readline().strip().split(' '))
    graph = Graph(n,types)
    mapHeap = MapHeap()
    for a1 in xrange(m):
        x,y,r = raw_input().strip().split(' ')
        x,y,r = [int(x),int(y),int(r)]
        graph.addEdge(x,y,r)
        mapHeap.insert(x,INF)
        mapHeap.insert(y,INF)
    s,d,k = map(int,raw_input().strip().split(' '))
    #s,d,k = [int(s),int(d)]
    print graph.graph
    print dijkstraShortestPath(n,graph,mapHeap,s,k)
"""
