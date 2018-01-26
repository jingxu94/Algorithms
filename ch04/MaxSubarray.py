#__author:  "Jing Xu"
#date:  2018/1/26

import math

def find_max_crossing_subarray( Array, low, mid, high ):
	'''
	分治策略求最大子数组中寻找跨越中间一点最大子数组子过程
	:param Array: 待搜索数组
	:param low: 左端点
	:param mid: 中间点
	:param high: 右端点
	:return: 跨越中间点构成的子数组中和最大的左端点，右端点，最大和值
	'''
	left_sum = -math.inf
	sum = 0
	for i in range( mid, low-1, -1 ):
		sum += Array[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i
	right_sum = -math.inf
	sum = 0
	for j in range( mid+1, high+1 ):
		sum += Array[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j
	return max_left, max_right, left_sum+right_sum


def find_maximum_subarray( Array, low, high ):
	'''
	分治算法求解最大子数组问题
	:param Array: 待求解数组
	:param low: 左端点
	:param high: 右端点
	:return: 最大子数组的左端点，右端点，最大和值
	'''
	flag = True
	for i in range(low,high+1):
		if Array[i] > 0:
			flag = False
	if flag:
		return None, None, 0
	elif high == low:
		return low, high, Array[low]
	else:
		mid = ( low+high )//2
		left_low, left_high, left_sum = find_maximum_subarray( Array, low, mid )
		right_low, right_high, right_sum = find_maximum_subarray( Array, mid+1, high )
		cross_low, cross_high, cross_sum = find_max_crossing_subarray( Array, low, mid, high )
		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_low, left_high, left_sum
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return  right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_subarray = find_maximum_subarray( A, 0, 15 )
print(max_subarray)
B = [-12, -4, -5, -8, -3, -10, -20]
max_subarray1 = find_maximum_subarray( B, 0, 6 )
print(max_subarray1)