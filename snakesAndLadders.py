import time

def reachtheEnd(cur_pos,end_pos,ladders,snakes,moves,final_result,reachLadder=None):
	if cur_pos == end_pos:
		#print "Moves till here:",moves
		if end_pos == 100:
			if len(final_result)==0:
				final_result.add(moves)
			elif moves < min(final_result):
				final_result.add(moves)
		return moves

	min_move = end_pos-cur_pos
	for i in range(6,0,-1):
		safe = True
		print "cur_pos,i:",(cur_pos,i)
		for snake in snakes:
			if snake[0]==cur_pos+i and snake[0]!=reachLadder:
				print "Not Safe,",snake,cur_pos+i
				safe = False
				break
		if safe==False:
			continue

		for ladder in ladders:
			if ladder[0]==cur_pos+i and ladder[0]!=reachLadder:
				print "Not Allowed"
				safe = False
				break

		if safe and cur_pos+i<=end_pos:
			return reachtheEnd(cur_pos+i,end_pos,ladders,snakes,moves+1,final_result,reachLadder)
	return -1

def quickestWayUpUtil(cur_pos,ladders,snakes,moves,visitedSnakeLadders,final_result):
	#search for ladders and snakes in visinity
	print "cur_pos:",cur_pos
	#time.sleep(0.02)
	ladderMoves = 100
	for ladder in ladders:
		if ladder[0] > cur_pos and ladder[0] not in visitedSnakeLadders[0]:
			tempMoves = reachtheEnd(cur_pos,ladder[0],ladders,snakes,0,final_result,ladder[0])
			visitedSnakeLadders[0].add(ladder[0])
			#print "tempMoves:",tempMoves
			#time.sleep(0.2)
			tempMoves = quickestWayUpUtil(ladder[1],ladders,snakes,moves+tempMoves,visitedSnakeLadders,final_result)
			ladderMoves = min(ladderMoves,tempMoves)
			visitedSnakeLadders[0].remove(ladder[0])
	
	if ladderMoves < 100:
		moves = ladderMoves
	val1 = reachtheEnd(cur_pos,100,ladders,snakes,moves,final_result,None)
	
	#Get bitten by available snakes
	print "Going to bitten by snake,final_result:",final_result
	for snake in snakes:
		#time.sleep(0.2)
		if snake[0] > cur_pos and snake[0] not in visitedSnakeLadders[1]:
			tempMoves = reachtheEnd(cur_pos,snake[0],ladders,snakes,0,final_result,snake[0])
			visitedSnakeLadders[1].add(snake[0])
			tempMoves = quickestWayUpUtil(snake[1],ladders,snakes,moves+tempMoves,visitedSnakeLadders,final_result)
			ladderMoves = min(ladderMoves,tempMoves)
	#No Ladders remaining. Now simply reach the end without bitten by snake
	if ladderMoves < 100:
		moves = ladderMoves
	val2 = reachtheEnd(cur_pos,100,ladders,snakes,moves,final_result,None)
	return min(val1,val2)

def quickestWayUp(ladders,snakes):
	final_result = set()
	#Go for move
	visitedSnakeLadders = [set(),set()]
	quickestWayUpUtil(1,ladders,snakes,0,visitedSnakeLadders,final_result)
	print final_result
	if len(final_result):
		return min(final_result)
	return -1

ladders = [[32,62],[42,68],[12,98]]
snakes = [[95,13],[97,25],[93,37],[79,27],[75,19],[49,47],[67,17]]

#print quickestWayUp(ladders,snakes)

ladders01 = [[8,52],[6,80],[26,42],[2,72]]
snakes01 = [[51,19],[39,11],[37,29],[81,3],[59,5],[79,23],[53,7],[43,33],[77,21]]
#Expected Output: 5
print quickestWayUp(ladders01,snakes01)

ladders02 = [[3,54],[37,100]]
snakes02 = [[56,33]]
#Expected Output: 3, take ladder (3,54), get bitten by snake (56,33) take next ladder from there (37,100)
#print quickestWayUp(ladders02,snakes02)

ladders03 = [[3,90]]
snakes03 = [[99,10],[97,20],[98,30],[96,40],[95,50],[94,60],[93,70]]
#print quickestWayUp(ladders03,snakes03)

ladders04 = [[3,5],[7,8],[44,56],[36,54],[88,91],[77,83],[2,4],[9,99],[45,78],[31,75]]
snakes04 = [[10,6],[95,90],[96,30],[97,52],[98,86]]
#print quickestWayUp(ladders04,snakes04)
