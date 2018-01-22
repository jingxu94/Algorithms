#__author:  "Jing Xu"
#date:  2018/1/22

import math

def merge(A, p, q, r):
	llist = A[p:q+1]
	rlist = A[q+1:r+1]
	llist.append(math.inf)
	rlist.append(math.inf)
	i = 0
	j = 0
	inversions = 0
	for k in range(p,r+1):
		if llist[i] <= rlist[j]:
			A[k] = llist[i]
			i += 1
		else:
			A[k] = rlist[j]
			j += 1
			inversions += len(llist) - i - 1
	return inversions

def merge_sort(A, p, r):
	inversions = 0
	if p < r:
		q = (p+r)//2
		inversions += merge_sort(A, p, q)
		inversions += merge_sort(A, q+1 , r)
		inversions += merge(A, p, q, r)
	return inversions

A = [31,41,59,26,41,58,69,32,90,13,45,55]
print( merge_sort(A, 0 ,len(A)-1) )