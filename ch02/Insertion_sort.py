#__author:  "Jing Xu"
#date:  2018/1/21

def insertion_sort(A,order='Ascending'):
	list_length = len(A)
	if list_length < 2:
		return A
	for j in range(1,list_length):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	if order == 'Descending':
		for i in range(list_length//2):
			A[i],A[list_length-1-i] = A[list_length-1-i],A[i]
	return A

A = [31,41,59,26,41,58]
print( insertion_sort(A) )
print( insertion_sort(A,order='Descending') )