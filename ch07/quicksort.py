#__author:  "Jing Xu"
#date:  2018/1/30

import random

def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quicksort(A, p ,q-1)
		quicksort(A, q+1, r)
	return A

def partition(A, p, r):
	x = A[r]
	i = p - 1
	count = 0
	for j in range(p,r):
		if A[j] == x:
			count += 1
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i+1-count//2

def randomized_partition(A, p, r):
	i = random.randrange(p, r+1)
	A[r], A[i] = A[i], A[r]
	return partition(A, p, r)

def randomized_quicksort(A, p, r):
	if p < r:
		q = randomized_partition(A, p, r)
		randomized_quicksort(A, p, q-1)
		randomized_quicksort(A, q+1, r)
	return A


A = [31,41,59,26,41,58,69,32,90,13,45,55]
B = [31,41,59,26,41,58,69,32,90,13,45,55]
print(quicksort(A, 0, len(A)-1))
print(randomized_quicksort(B, 0, len(B)-1))
