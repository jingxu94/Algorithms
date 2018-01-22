#__author:  "Jing Xu"
#date:  2018/1/21

# 将两个二进制数相加
def add_binary(A,B):
	if len(A) > len(B):
		A, B = B, A
	C = B
	for i in range(len(A)):
		if A[i] + C[i] < 2:
			C[i] = A[i] + C[i]
		elif A[i] + C[i] == 2:
			C[i] = 0
			C[i+1] += 1
		else:
			C[i] = 1
			C[i+1] = 1
	for i in range(len(A),len(B)):
		if C[i] == 2:
			C[i] = 0
			C[i+1] += 1
	return C

# 将一个二进制数转换为十进制数
def binary_to_decimal(binary):
	decimal = 0
	for i in range(len(binary)):
		decimal += pow(2,i)*binary[i]
	return decimal

# 将一个十进制数转换为二进制数
def decimal_to_binary(decimal):
	i = 0
	binary = []
	while decimal//2 > 0:
		binary.append( decimal%2 )
		decimal = decimal//2
		i += 1
	if decimal == 1:
		binary.append( 1 )
	return binary

# 任意数量的二进制数相加求和，返回一个二进制数
def add_binary_plus(*args):
	addsum = 0
	for i in args:
		addsum += binary_to_decimal(i)
	return decimal_to_binary(addsum)

A = [1,0,1,0,0,0,1,0,1,0,0,1,1,1,0,1]
B = [1,1,1,0,1,0,0,0,1,0,1,0,1]
C = add_binary_plus(A,B)
print(C)
D = add_binary(A,B)
print(D)
print( add_binary_plus(A,B,C) )