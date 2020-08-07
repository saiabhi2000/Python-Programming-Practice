t = int(input())
for i in range(t):
	a = input()
	a = a.lower()
	if len(a) % 2 == 0:
			b = len(a) // 2
			s1 = a[:b]
			s2 = a[b:]
			if sorted(s1) == sorted(s2):
				print('YES')
			else:
				print('NO')
	else:
		b = len(a) // 2
		s3 = a[:b]
		s4 = a[(b+1):]
		if sorted(s3) == sorted(s4):
			print('YES')
		else:
			print('NO')
