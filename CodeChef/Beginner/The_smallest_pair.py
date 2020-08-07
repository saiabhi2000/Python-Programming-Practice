t = int(input())
for i in range(t):
	a = int(input())
	b = list(map(int,input().split()))
	b.sort()
	print(b[0] +b[1])
