N = int(input())
X = 0
Y = 0
winner = 0
for i in range (N):
	V,W  = input().split()
	V = int(V)
	W = int(W)
	X += V
	Y += W
	if (X - Y) > winner:
		U = 1
		winner = X-Y
	elif (Y - X) > winner: 
		U = 2
		winner = Y-X
print (U, winner)
		

	
