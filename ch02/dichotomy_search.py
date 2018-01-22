#__author:  "Jing Xu"
#date:  2018/1/22

import math

# 分治法排列两个序列，假定两个序列已排序，加入了哨兵牌来控制程序停止
def merge(A, p, q, r):
	llist = A[p:q+1]
	rlist = A[q+1:r+1]
	llist.append(math.inf)
	rlist.append(math.inf)
	i = 0
	j = 0
	for k in range(p,r+1):
		if llist[i] <= rlist[j]:
			A[k] = llist[i]
			i += 1
		else:
			A[k] = rlist[j]
			j += 1
	return A

def merge_sort(A, p, r):
	if p < r:
		q = (p+r)//2
		merge_sort(A, p, q)
		merge_sort(A, q+1 , r)
		merge(A, p, q, r)
	return A

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