t = int(input())
for i in range (t):
	a,b,c = input().split()
	a = int(a)
	b = int(b)
	c = int(c)
	if a>b and a>c:
		if b>c:
			print (b)
		if b<c:
			print (c)
	if b>a and b>c:
		if a>c:
			print (a)
		if a<c:
			print (c)
	if c>a and c>b:
		if a>b:
			print (a)
		if a<b:
			print (b)
