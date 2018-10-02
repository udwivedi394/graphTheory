#!/bin/python

import sys
INF = 10**8
class Graph:
        def __init__(self,vertices):
                self.graph = {}
                self.vertices = vertices

        def addEdge(self,u,v,data):
                if self.graph.get(u)==None:
                        self.graph[u] = {}
                
		value = self.graph[u].get(v)
                self.graph[u][v]= min(value,data) if value!=None else data
                
                if self.graph.get(v)==None:
                        self.graph[v] = {}
                
		value = self.graph[v].get(u)
                self.graph[v][u]= min(value,data) if value!=None else data
                return

def rustNMurderer(N,graph,start):
	notvisited = set(list(xrange(1,N+1)))
	vDistance = {}
	
	current = start
	notvisited.remove(current)
	while notvisited:
		if current == start:
			vDistance[current] = 0
		nextItr = None
		visited = set()
		for vertex in notvisited:
			flag = True
			if graph.graph.get(current)==None:
				flag = False
				
			if flag and graph.graph[current].get(vertex):
				continue

			visited.add(vertex)
			if nextItr == None:
				nextItr = vertex
			vDistance[vertex] = vDistance[current]+1

		notvisited=notvisited.difference(visited)
		current = nextItr if nextItr else current+1
        for i in range(1,N+1):
                if i!=start:
                        print vDistance[i],
	return


f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/rustNMurdererTestCase.txt", 'r')
t = int(f1.readline().strip())
for a0 in xrange(t):
    n,m = f1.readline().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = Graph(n)
    #mapHeap = MapHeap()
    for a1 in xrange(m):
        x,y = f1.readline().strip().split(' ')
        x,y = [int(x),int(y)]
        graph.addEdge(x,y,INF)
        #mapHeap.insert(x,INF)
        #mapHeap.insert(y,INF)
    s = int(f1.readline().strip())
    #print graph.graph
    rustNMurderer(n,graph,s)
    print

"""
t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    graph = Graph(n)
    #mapHeap = MapHeap()
    for a1 in xrange(m):
        x,y = raw_input().strip().split(' ')
        x,y = [int(x),int(y)]
        graph.addEdge(x,y,INF)
        #mapHeap.insert(x,INF)
        #mapHeap.insert(y,INF)
    s = int(raw_input().strip())
    #print graph.graph
    rustNMurderer(n,graph,s)
    print
"""
