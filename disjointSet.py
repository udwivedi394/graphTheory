#Space Complexity: O(n)
#Time complexity: If there are m operations and n elements
#Then time complexity: O(ma(n)), here a = alpha
#In most of the practical cases, a(n) <= 4
#Therefore, overall time complexity is equivalent to O(m)
class Node:
	def __init__(self,data):
		self.data = data
		self.rank = 0
		self.parent = self

	#Return the overall Rank of current set
	def findRank(self):
		temp = self.findSet()
		return temp.rank
	
	#Find the main representative set of current set
	def findSet(self):
		temp = self.parent
		while temp.parent != temp:
			temp = temp.parent
		#Path Compression, set the parent of current pointer to the representative set directly
		self.parent = temp
		return temp

	#Print the current hierarchy of current set, bottom's up
	def printSet(self):
		temp = self
		while 1:
			print temp.data,
			if temp.parent == temp:
				break
			temp = temp.parent

#Make a new set
def makeSet(data):
	return Node(data)

#Merge two sets
def union(set1,set2):
	#If the rank of both the sets is same, then
	if set1.findRank() == set2.findRank():
		#Set the parent of representative of set2 to representative of set1
		set2.findSet().parent = set1.findSet()
		#Increment the overall rank of set1 by 1
		set1.findSet().rank += 1
	elif set1.findRank() > set2.findRank():
		#Set the parent of representative of set2 to representative of set1
		set2.findSet().parent = set1.findSet()
	else:
		#Set the parent of representative of set1 to representative of set2
		set1.findSet().parent = set2.findSet()

#Creating Lookup
s = {}
for i in range(8):
	s[i]=makeSet(i)

union(s[1],s[2])
union(s[2],s[3])
union(s[4],s[5])
union(s[6],s[7])
union(s[5],s[6])
union(s[3],s[7])

for i in range(len(s)):
	print "\nSet:%d,Rank:%d,findSet:%d"%(i,s[i].rank,s[i].findSet().data)
	s[i].printSet()
