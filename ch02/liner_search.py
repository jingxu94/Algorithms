#__author:  "Jing Xu"
#date:  2018/1/21

def liner_search(A,v):
	for i in range(len(A)):
		if A[i] == v:
			return i+1

A = [31,41,59,26,41,58]
print( liner_search(A,66) )
print( liner_search(A,26) )