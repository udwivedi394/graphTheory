import time

if __name__ == "__main__":
	try:
		#File generated after running the program
		f1 = open("travelHackerOutput.txt",'r')
		f2 = open("travelHackerOutput#1.txt",'r')
		count = 0

		while 1:
			line1 = f1.readline()
			line2 = f2.readline()
			
			if line1 != line2 or line1==None or line2==None:
				print line1, line2
				break
			if count>1000:
				break
			count += 1
		print count
	finally:
		f1.close()
		f2.close()
