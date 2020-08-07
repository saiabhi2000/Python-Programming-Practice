t = int(input())
for i in range(t):
	bs = int(input())
	hra = 0
	da = 0
	gs = hra + da +bs
	if bs < 1500:
		hra = float(bs * 0.1)
		da = float(bs * 0.9)
		gs = hra + da +bs
		print('%.2f' %gs)
	elif bs >= 1500:
		hra = 500
		da = float(bs * 0.98)
		gs = hra + da +bs
		print('%.2f' %gs)
		
	
