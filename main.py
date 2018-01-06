import directedGraph as dirG
import undirectedGraph as undirG

#Driver program for undirected Graph
print "\n------------------------"
print "UnDirected Graphs"
graph1 = undirG.UnDirGraph(5)
graph1.addEdge(0,1)
graph1.addEdge(0,4)
graph1.addEdge(1,2)
graph1.addEdge(1,3)
graph1.addEdge(1,4)
graph1.addEdge(2,3)
graph1.addEdge(3,4)

graph1.printGraph()
print "\nBFS:"
graph1.BFS(0)
print "\nDFS:"
graph1.DFS(0)

graph2 = undirG.UnDirGraph(4)
graph2.addEdge(0,1)
graph2.addEdge(0,2)
graph2.addEdge(1,2)
graph2.addEdge(2,0)
graph2.addEdge(2,3)
graph2.addEdge(3,3)

graph2.printGraph()
print "\nBFS:"
graph2.BFS(0)
print "\nDFS:"
graph2.DFS(0)

g3 = undirG.UnDirGraph(7)
g3.addEdge(1,3)
g3.addEdge(1,2)
g3.addEdge(2,5)
g3.addEdge(2,4)
g3.addEdge(3,5)
g3.addEdge(4,6)
g3.addEdge(4,5)
g3.addEdge(5,6)

g3.printGraph()
print "\nBFS:"
g3.BFS(1)
print "\nDFS:"
g3.DFS(1)

#Directed graph
print "\n------------------------"
print "Directed Graphs"
graph1 = dirG.DirectedGraph()
graph1.addEdge(0,1)
graph1.addEdge(0,4)
graph1.addEdge(1,2)
graph1.addEdge(1,3)
graph1.addEdge(1,4)
graph1.addEdge(2,3)
graph1.addEdge(3,4)

graph1.printGraph()
print "\nBFS:"
graph1.BFS(0)
print "\nDFS:"
graph1.DFS(0)

graph2 = dirG.DirectedGraph()
graph2.addEdge(0,1)
graph2.addEdge(0,2)
graph2.addEdge(1,2)
graph2.addEdge(2,0)
graph2.addEdge(2,3)
graph2.addEdge(3,3)

graph2.printGraph()
print "\nBFS:"
graph2.BFS(2)
print "\nDFS:"
graph2.DFS(2)

g3 = dirG.DirectedGraph()
g3.addEdge(1,3)
g3.addEdge(1,2)
g3.addEdge(2,5)
g3.addEdge(2,4)
g3.addEdge(3,5)
g3.addEdge(4,6)
g3.addEdge(4,5)
g3.addEdge(5,6)

g3.printGraph()
print "\nBFS:"
g3.BFS(1)
print "\nDFS:"
g3.DFS(1)
