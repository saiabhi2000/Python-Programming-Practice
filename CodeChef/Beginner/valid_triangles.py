t = int(input())
for i in range(t):
	a = sum(map(int, input().split()))
	if (a == 180):
		print ("YES")
	else:
		print("NO") 
