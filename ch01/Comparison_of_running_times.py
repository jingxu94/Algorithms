#__author:  "Jing Xu"
#date:  2018/1/21

import math

def f(n):
	return math.log(n,2)

def f0(n):
	return n

def f1(n):
	return n*math.log(n,2)

def f2(n):
	return n*n

def f3(n):
	return n*n*n

def f4(n):
	return pow(2,n)

def f5(n):
	if n == 1:
		return 1
	else:
		return n*f5(n-1)

def max_num_pertime(func,time):
	max_num = 1
	while func(max_num) < time:
		max_num += 1
	return max_num

# print(max_num_pertime(f,1000))
print(max_num_pertime(math.sqrt,1000))
print(max_num_pertime(f0,1000))
print(max_num_pertime(f1,1000))
print(max_num_pertime(f2,1000))
print(max_num_pertime(f3,1000))
print(max_num_pertime(f4,1000))
print(max_num_pertime(f5,1000))