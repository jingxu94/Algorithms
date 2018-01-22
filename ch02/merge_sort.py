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

# 分治法排列两个序列，假定两个序列已排序，不使用哨兵牌，Exercises 2.3-2
def merge_v1(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	llist = A[p:q+1]
	rlist = A[q+1:r+1]
	i = 0
	j = 0
	for k in range(p,r+1):
		if i == n1:
			A[k:r+1] = rlist[j:n2]
			break
		elif j == n2:
			A[k:r+1] = llist[i:n1]
			break
		elif llist[i] <= rlist[j]:
			A[k] = llist[i]
			i += 1
		else:
			A[k] = rlist[j]
			j += 1
	return A

# 分治法排序，A为待排序序列，p为起始排序角标，r为终止排序角标
def merge_sort(A, p, r):
	if p < r:
		q = (p+r)//2
		merge_sort(A, p, q)
		merge_sort(A, q+1 , r)
		merge(A, p, q, r)
	return A

# 分治法排序，调用不使用哨兵牌判断结束的版本
def merge_sort_v1(A, p, r):
	if p < r:
		q = (p+r)//2
		merge_sort_v1(A, p, q)
		merge_sort_v1(A, q+1 , r)
		merge_v1(A, p, q, r)
	return A

A = [31,41,59,26,41,58,69,32,90,13,45,55]
print( merge_sort_v1(A, 0 ,len(A)-1) )
print( merge_sort(A, 0, len(A)-1) )
