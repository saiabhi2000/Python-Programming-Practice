t = int(input())
c = []
for i in range(t):
	a,b = map(int,input().split())
	if a > 1000:
		a = a - (a*0.1)
	c.append(a * b)
for i in c:
	print("%.6f" %i)
