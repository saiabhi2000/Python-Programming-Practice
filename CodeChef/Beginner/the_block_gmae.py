t = int(input())
for i in range (t):
	s = input()
	if (s == s[::-1]):
		print("wins")
	else:
		print("loses")
