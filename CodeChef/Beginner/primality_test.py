t = int(input())
for i in range(t):
	a = int(input())
	count = 1
	for j in range(2, int(sqrt(a+1))):
		if int(a % j == 0):
			print("no")
			count = 2
			break
	if(count == 1) and (a != 1):
		print("yes")
	if(a == 1):
		print("no")
