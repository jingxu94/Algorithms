#__author:  "Jing Xu"
#date:  2018/1/22

from merge_sort import merge_sort

def dichotomy_search(A,v):
	merge_sort(A, 0, len(A)-1)
	start = 0
	end = len(A) - 1
	while start <= end:
		mid = int((end+start)/2)
		if A[mid] < v:
			start = mid + 1
		elif A[mid] > v:
			end = mid - 1
		else:
			return mid

A = [31,41,59,26,41,58,69,32,90,13,45,55]
print( dichotomy_search(A,41) )
print(A)