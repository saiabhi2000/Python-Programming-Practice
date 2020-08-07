N = int(input())
for i in range (N):
	number = int(input())
	sum = 0
	while number != 0:
		a = number%10 
		sum += a;
		number = int(number/10)
	print(sum)
