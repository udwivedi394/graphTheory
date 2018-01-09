import time

def isSafe(arr,visited,row,col):
	m = len(arr)
	n = len(arr[0])
	
	if row >= m or row < 0 or col >= n or col < 0 or visited[row][col]==True or arr[row][col] == 0:
		return False
	if visited[row][col]==False and arr[row][col]==1:
		return True

def findIslands(arr):
	m = len(arr)
	n = len(arr[0])
	
	visited = [[False for i in range(n)] for j in range(m)]
	no_of_islands = 0

	for i in range(m):
		for j in range(n):
			if isSafe(arr,visited,i,j):
				findIslandsUtil(arr,visited,i,j)
				no_of_islands += 1
	return no_of_islands

#x-> moves in direction of column
#y-> moves in direction of row
def findIslandsUtil(arr,visited,row,col):
	move_y = [-1,-1,-1, 0, 1, 1, 1, 0]
	move_x = [-1, 0, 1, 1, 1, 0,-1,-1]
	
	visited[row][col]=True

	for i in range(8):
		if isSafe(arr,visited,row+move_y[i],col+move_x[i]):
			findIslandsUtil(arr,visited,row+move_y[i],col+move_x[i])
	return

arr=[[1,1,0,0,0],
     [0,1,0,0,1],
     [1,0,0,1,1],
     [0,0,0,0,0],
     [1,0,1,0,1]]

print "Number of Islands:",findIslands(arr)
