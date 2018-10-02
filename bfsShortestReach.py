#!/bin/python

import sys
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
INF = 10**8

class Graph:
        def __init__(self,vertices):
                self.graph = {}
                self.vertices = vertices

        def addEdge(self,u,v):
		if self.graph.get(u)==None:
			self.graph[u] = set()
		if self.graph.get(v)==None:
			self.graph[v] = set()

                self.graph[u].add(v)
                self.graph[v].add(u) 
                return
            
def bfs(N,graph,mapHeap,start):
	mapHeap.setData(start,0)
	vDistance = {}
	
	while len(mapHeap.arr):
                current = mapHeap.extractMin()
                mapHeap.delete(current[0])

                vDistance[current[0]] = current[1]
                for neighbour in graph.graph[current[0]]:
                        pos = mapHeap.contains(neighbour)
                        if pos==None:
                                continue
                        if mapHeap.arr[pos][1] > current[1]+6:#vDistance[current[0]]+prev_data:
                                mapHeap.setData(neighbour, current[1]+6)#vDistance[current[0]]+prev_data)
                                
        for i in range(1,N+1):
                if i!=start:
                        print vDistance.get(i) if vDistance.get(i) not in (None,INF) else -1,
	return

f1 = open("/home/utkarsh/Documents/bfstestcase.txt",'r')

t = int(f1.readline().strip())
for a0 in xrange(t):
    n,m = f1.readline().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = Graph(n)
    mapHeap = MapHeap()
    for a1 in xrange(m):
        x,y = f1.readline().strip().split(' ')
        x,y = [int(x),int(y)]
        graph.addEdge(x,y)
        mapHeap.insert(x,INF)
        mapHeap.insert(y,INF)
    s = int(f1.readline().strip())
    #print mapHeap.lookup
    #print graph.graph
    bfs(n,graph,mapHeap,s)
    print
'''
t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = Graph(n)
    mapHeap = MapHeap()
    for a1 in xrange(m):
        x,y = raw_input().strip().split(' ')
        x,y = [int(x),int(y)]
        graph.addEdge(x,y)
        mapHeap.insert(x,INF)
        mapHeap.insert(y,INF)
    s = int(raw_input().strip())
    #print mapHeap.lookup
    #print graph.graph
    bfs(n,graph,mapHeap,s)
    print
'''
