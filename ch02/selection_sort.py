#__author:  "Jing Xu"
#date:  2018/1/22

def selection_sort(A):
	for i in range(len(A)-1):
		min = A[i]
		flag = i
		for j in range(i+1,len(A)):
			if A[j] < min:
				min = A[j]
				flag = j
		A[i], A[flag] = min, A[i]
	return A

A = [31,41,59,26,41,58,69,32,90,13,45,55]
print( selection_sort(A) )
