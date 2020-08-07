t = int(input())
if t <= 50:
	for i in range(t):
		a, b = map(int, input().split())
		print(max([a % j for j in range(1, b + 1)]))

