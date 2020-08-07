t = int(input())
count, i = 0, 12
for i in range(t):
	p = int(input())
	while p > 0:
		if 2 ** i >= p :
			p -= 2 ** i
			count = count + 1
			if 2 ** i >= p : continue
		i = i - 1
		
	print(count) 
	
	
	
