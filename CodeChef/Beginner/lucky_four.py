T = int(input())
for i in range(T):
	Count = 0
	A = input()
	for j in A:
		if j == '4':
			Count += 1
		else:
			continue
	print(Count)
