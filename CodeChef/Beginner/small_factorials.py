T = int(input())

for i in range(T):
	A = int(input())
	output = 1
	for j in range(1, A+1):
		output*=j
	print(output)		
