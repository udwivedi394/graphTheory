#!/bin/python

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
                visited = set()
                for key in self.graph:
                        if key not in visited:
                                stack = [key]
                                count = 0 
                                while stack:
                                        current = stack.pop()
                                        if current not in visited:
                                                count += 1
    
                                        visited.add(current)
    
                                        for neighbour in self.graph[current]:
                                                if neighbour not in visited:
                                                        stack.append(neighbour)
                                if self.connectedComp.get(count)==None:
                                        self.connectedComp[count] = 0 
                                self.connectedComp[count] += 1 
                if self.connectedComp.get(1)==None:
                        self.connectedComp[1]=0
                self.connectedComp[1]+=(self.vertices-len(visited))
                return

def roadsAndLibraries(n, c_lib, c_road, country):
        country.connectedComponents()
        cost = 0
        for i,count in country.connectedComp.iteritems():
                if i==1:
                        cost += count*c_lib
                else:
                        cost += (min((i-1)*c_road+c_lib,i*c_lib))*count
        return cost
if __name__ == "__main__":
	f1 = open("/home/utkarsh/utk_reboot/python/graphTheory/roadsNLibTestCase.txt",'r') 
	q = int(f1.readline().strip())
   	for a0 in xrange(q):
		n, m, c_lib, c_road = f1.readline().strip().split(' ')
		n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
		if c_lib > c_road:
			country = Graph(n)
		for cities_i in xrange(m):
			x,y = map(int,f1.readline().strip().split(' '))
                	if c_lib > c_road:
				country.addEdge(x,y)
        	if c_lib < c_road:
			print n*c_lib
        	else:
            		print roadsAndLibraries(n, c_lib, c_road, country)

"""
if __name__ == "__main__":
    q = int(sys.stdin.readline().strip())
    for a0 in xrange(q):
        n, m, c_lib, c_road = sys.stdin.readline().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        if c_lib > c_road:
            country = Graph(n)

        for cities_i in xrange(m):
                x,y = map(int,sys.stdin.readline().strip().split(' '))
                if c_lib > c_road:
                    country.addEdge(x,y)
        if c_lib < c_road:
            print n*c_lib
        else:
            print roadsAndLibraries(n, c_lib, c_road, country)
"""
