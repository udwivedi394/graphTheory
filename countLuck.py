#Here we just have to find path, and whenver we are faced with multiple choices
#!/bin/python

import sys
#x-> movement in column direction, y->movement in row direction
#arr[y][x] -> element in yth row, xth column
def isSafe(n,m,matrix,curmv_y,curmv_x):
	if curmv_x < 0 or curmv_y < 0 or curmv_x > m-1 or curmv_y > n-1:
		return False
	try:
		if matrix[curmv_y][curmv_x] in ('.','*'):
			return True
	except Exception as e:
		print e, "y:",curmv_y,"x:",curmv_x
	return False

def countLuckUtil(n,m,matrix,curpos_y,curpos_x,prevmv,luckcount):
	if matrix[curpos_y][curpos_x] == '*':
		return luckcount	

	#print "At pos:",(curpos_y,curpos_x)
	posmv_y = [0, 1, 0,-1]
	posmv_x = [1, 0,-1, 0]
	
	avail_dir = []
	for i in range(4):
		if isSafe(n,m,matrix,curpos_y+posmv_y[i],curpos_x+posmv_x[i]) and \
			(curpos_y+posmv_y[i],curpos_x+posmv_x[i])!=prevmv:
			avail_dir.append(i)
	
	if len(avail_dir)>1:
		luckcount += 1

	tempmv = (curpos_y,curpos_x)
	for i in avail_dir:
		temp = countLuckUtil(n,m,matrix,curpos_y+posmv_y[i],curpos_x+posmv_x[i],tempmv,luckcount)
		if temp != -1:
			return temp
	return -1

def countLuck(n,m,matrix,start_pos):
	return countLuckUtil(n,m,matrix,start_pos[0],start_pos[1],None,0)

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
	start_pos = None
        n, m = raw_input().strip().split(' ')
        n, m = [int(n), int(m)]
        matrix = []
        matrix_i = 0
        for i in xrange(n):
            matrix_t = str(raw_input().strip())
	    if 'M' in matrix_t:
		start_pos = (i,matrix_t.index('M'))
            matrix.append(matrix_t)
        result = countLuck(n,m,matrix,start_pos)
        k = int(raw_input().strip())
	if result==k:
		print "Impressed"
	else:
		print "Oops!"
